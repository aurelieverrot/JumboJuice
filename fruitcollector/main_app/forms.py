from django.forms import ModelForm
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
        fields = ('email', 'id')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'fav_juice')

