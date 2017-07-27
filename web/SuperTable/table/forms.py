from django import forms
from table.models import SearchResult

class SearchForm(forms.Form):
    year = forms.IntegerField()
    semester = forms.CharField()
    course = forms.CharField()
    courseNum = forms.IntegerField()
    