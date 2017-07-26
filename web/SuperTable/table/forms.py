from django import forms

class SearchForm(forms.Form):
    year = forms.IntegerField()
    semester = forms.CharField()
    course = forms.CharField()
    courseNum = forms.IntegerField()