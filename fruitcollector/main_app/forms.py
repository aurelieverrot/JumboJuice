from django.forms import ModelForm
from .models import Juice, Fruit, Profile, Vitamin

class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'vitamins']

class JuiceForm(ModelForm):
    class Meta:
        model = Juice
        fields = ['name', 'description', 'drink_type', 'fruits']

class ProfileForm(ModelForm):
    pass
  # to allow User to edit or delete the profile
  
class VitaminForm(ModelForm):
    class Meta:
        model = Vitamin
        fields = ['name']