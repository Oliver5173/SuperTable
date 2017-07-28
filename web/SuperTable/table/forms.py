from django import forms
from table.models import SearchResult

class SearchForm(forms.Form):
    year = forms.IntegerField()
    semester = forms.CharField()
    courseInfo = forms.CharField()

    class Meta:
        model = SearchResult

    def __init__(self, *args, **kwargs):
        pass