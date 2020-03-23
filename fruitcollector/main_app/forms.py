from django.forms import ModelForm
from django import forms
from .models import Juice, Fruit, Profile
from django.contrib.auth.models import User


class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = ['name']

class JuiceForm(ModelForm):
    class Meta:
        model = Juice
        fields = ['name', 'description', 'drink_type', 'fruits']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name')
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'fav_juice')
        # shows the labels in html
        labels = {
            'bio': 'About me', 
            'fav_juice': 'My favorite juice'
            }
     

