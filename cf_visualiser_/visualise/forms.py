from django import forms

class search_handle(forms.Form):
    name = forms.CharField(label='Handle', max_length=35)
