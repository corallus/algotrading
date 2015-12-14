import os
from fabric.api import env, run, prompt, local, get, sudo
import wolderwijd.settings as settings
from fabric.contrib.project import rsync_project
from fabric.colors import blue, red

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
VIRTUAL_ENVIRONMENT = settings.VIRTUAL_ENVIRONMENT

env.domain = ''
env.environment = ''
env.hosts = ['109.70.6.143']
env.repository = 'git@github.com:corallus/algotrading.git'


def live():
    """ chooses live environment """
    env.environment = ""
    env.user = ''
    env.path = '/home/%(user)s/domains/%(domain)s/%(environment)s' % env
    env.settings_path = '%s/algotrading' % env.path
    env.media_path = '%s/media' % env.path


def restart():
    """ chooses live environment """
    env.user = 'root'
    sudo('service httpd restart')


def reset_local_db():
    """ resets local database """

    print(red(" * deleting local database..."))
    local('mysql -u %s -p%s -e "drop database if exists %s"' % (
        settings.DATABASES['default']['USER'],
        settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['NAME']
    ))

    print(red(" * creating local database..."))
    local('mysql -u %s -p%s -e "create database %s"' % (
        settings.DATABASES['default']['USER'],
        settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['NAME']
    ))

    print(red(" * migrating local database..."))
    local('cd %s '
          '&& . %s '
          '&& python manage.py migrate' % (PROJECT_PATH, VIRTUAL_ENVIRONMENT))


def pull():
    """ updates development environment """

    x = prompt(blue('Reset local database (r) or flush (f)?'), default="f")

    if x == 'r':
        reset_local_db()
    elif x == 'f':
        print(red(" * flushing database..."))
        local('cd %s '
              '&& . %s '
              '&& python manage.py flush' % (PROJECT_PATH, VIRTUAL_ENVIRONMENT))

    print(red(" * creating database dump..."))
    run('cd %s '
        '&& source venv/bin/activate '
        '&& python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission > data.json' % env.path)

    print(red(" * downloading dump..."))
    get('%s/data.json' % env.path, '/tmp/data.json')

    print(red(" * importing the dump locally..."))
    local('cd %s '
          '&& . %s '
          '&& python manage.py loaddata /tmp/data.json' % (PROJECT_PATH, VIRTUAL_ENVIRONMENT), capture=False)

    print(red(" * removing database dump..."))
    run('rm %s/data.json' % env.path)

    print(red(" * syncing media files..."))
    rsync_project('%s/' % env.media_path, settings.MEDIA_ROOT, upload=False, delete=True)


def deploy():
    """ updates the chosen environment """

    print(red(" * updating code..."))
    run('cd %s && git pull' % env.path)

    if "y" == prompt(blue('Update packages (y/n)?'), default="y"):
        print(red(" * updating packages..."))
        run('cd %s '
            '&& source venv/bin/activate '
            '&& pip install -r requirements.txt' % env.path)

    if "y" == prompt(blue('Migrate database schema (y/n)?'), default="y"):
        print(red(" * migrating database schema..."))
        run('cd %s '
            '&& source venv/bin/activate '
            '&& python manage.py migrate' % env.path)

    print(red(" * collecting static files..."))
    run('cd %s '
        '&& source venv/bin/activate '
        '&& python manage.py collectstatic --noinput' % env.path)


def setup():
    if "y" == prompt(blue('Clone repository?'), default="y"):
        run('git clone %(repository)s %(path)s' % env)

    if "y" == prompt(blue('Create media folder?'), default="y"):
        run('mkdir %s' % env.media_path)
        run('chmod -R 777 %s' % env.media_path)

    if "y" == prompt(blue('Create virtual environment'), default="y"):
        run('cd %s '
            '&& virtualenv-2.7 venv --no-site-packages '
            '&& source venv/bin/activate '
            '&& pip install -r requirements.txt' % env.path)

    if "y" == prompt(blue('Create local_settings.py?'), default="y"):
        run('cd %s '
            '&& touch local_settings.py ' % env.settings_path)

        if "y" == prompt(blue('Edit local_settings.py now and press y to continue?'), default="y"):
            pass

    if "y" == prompt(blue('Migrate database?'), default="y"):
        run('cd %s '
            '&& source venv/bin/activate '
            '&& python manage.py migrate' % env.path)
