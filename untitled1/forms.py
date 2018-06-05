from django import forms


class YourNumber(forms.Form):
    your_number = forms.CharFieldField()
