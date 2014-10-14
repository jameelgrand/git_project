from django import forms
from django.forms import ModelForm
from importings.models import activedb,activefile
class dbform(ModelForm):
    class Meta:
        model = activedb
class fileform(ModelForm):
    class Meta:
        model = activefile
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
