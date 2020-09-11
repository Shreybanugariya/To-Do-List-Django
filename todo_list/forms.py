from django import forms
from .models import List

class ListForms(forms.ModelForm):
  item = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mr-sm-2 col-12','placeholder':'title'}))
  dsc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mr-sm-2 col-12', 'placeholder':'descritption', 'rows':3}))

  class Meta:
    model = List
    fields = ["item","dsc"]


class AddForm(forms.ModelForm):
  item = forms.CharField(widget=forms.TextInput(attrs={'class':'btn btn-outline-secondary my-2 my-sm-0'}))

  class Meta:
    model = List
    fields = ["item"]