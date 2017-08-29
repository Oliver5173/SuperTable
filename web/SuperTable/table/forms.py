from django import forms
from table.models import SearchResult

class SearchForm(forms.Form):
    year = forms.IntegerField()
    semester = forms.CharField()
    courseInfo = forms.CharField()