from django.forms import ModelForm
from django import forms
from .models import Juice, Fruit, Profile, Vitamin, VITAMIN_TYPES

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
  
class AddVitaminForm(forms.Form):
    vitamins = forms.ModelMultipleChoiceField(queryset=Vitamin.objects.all())