from django import forms
from django.forms import extras
from django.utils import timezone

from .models import Place


class NewPlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['name']


class UpdatePlaceForm(forms.ModelForm):

    def clean(self):
        # Always set visited if a value was set for date_visited
        cleaned_data = self.cleaned_data
        if cleaned_data.get('date_visited'):
            cleaned_data['visited'] = True

    class Meta:
        model = Place
        fields = ['name', 'visited', 'date_visited', 'notes']
        widgets = {'visited': forms.HiddenInput(),
                   'date_visited': extras.SelectDateWidget(years=range(2000, timezone.now().year + 1))
                   }


