from django import forms

from .models import Hotel


# class HotelForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     stars = forms.IntegerField(validators=[validate_hotel_stars])

class HotelModelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "stars", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"size": 500, 'class': 'special', "required": False})
        }

