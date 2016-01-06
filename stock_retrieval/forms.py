from django import forms
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse_lazy
from crispy_forms.layout import Submit

from .models import Share


class SyncFeedForm(forms.Form):
    pass


class CreateShareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateShareForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse_lazy('stock-create')
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Share
        exclude = []