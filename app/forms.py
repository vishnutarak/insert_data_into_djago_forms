from django import forms

class SchoolForm(forms.Form):
    name=forms.CharField(max_length=100)
    principal=forms.CharField(max_length=100)
    Location=forms.CharField(max_length=100)
    