from django import forms

class HotelForm(forms.Form):
    name = forms.CharField(max_length=50)
    stars = forms.IntegerField()

