from django.forms import ModelForm
from .models import Smoothie, Fruit

class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'region', 'description')

class SmoothieForm(ModelForm):
    class Meta:
        model = Smoothie
        fields = ['name', 'description', 'drink_type']