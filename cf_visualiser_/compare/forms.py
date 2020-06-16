from django import forms

class compare_handles(forms.Form):
    name1 = forms.CharField(label='Handle1', max_length=35)
    name2 = forms.CharField(label='Handle2', max_length=35)