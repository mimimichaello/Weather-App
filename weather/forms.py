from django import forms
from .models import SearchHistory
from dal import autocomplete

class SearchForm(forms.Form):
    city = forms.CharField(max_length=255, widget=autocomplete.ListSelect2(url='city-autocomplete'))
