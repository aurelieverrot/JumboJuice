from django.forms import ModelForm
from .models import Juice, Fruit, Profile

class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = ['name']

class JuiceForm(ModelForm):
    class Meta:
        model = Juice
        fields = ['name', 'description', 'drink_type', 'fruits']


class ProfileForm(ModelForm):
    pass
  # to allow User to edit or delete the profile