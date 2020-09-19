from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['restaurant',]


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['owner',]

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
