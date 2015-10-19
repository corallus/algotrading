from django.db import models
from django.utils.translation import ugettext_lazy as _


class Stock(models.Model):
    display_name = models.CharField(verbose_name=(_('stock')), max_length=127)
