from django import forms

class ComposeForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    to = forms.EmailField()
    