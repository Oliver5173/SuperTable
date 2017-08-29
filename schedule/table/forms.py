from django import forms

class courseForm(forms.Form):
    year = forms.CharField()
    semester = forms.CharField()
    content = forms.CharField()
