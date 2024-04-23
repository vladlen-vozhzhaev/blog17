from django import forms
class RegForm(forms.Form):
    name = forms.CharField(label="name")
    email = forms.CharField(label="email")
    password = forms.CharField(label="pass")