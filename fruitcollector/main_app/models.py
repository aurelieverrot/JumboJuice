from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

DRINK_TYPES = (
    ('G', 'Greens'),
    ('D', 'Detox'),
    ('S', 'Sweet')
)
VITAMIN_TYPES = (
  ('A', 'Necessary for proper vision and organ function.'),
  ('B1', 'Helps convert nutrients into energy.'),
  ('B2', 'Necessary for energy production, cell function and fat metabolism.'),
  ('B3', 'Drives the production of energy from food.'),
  ('B5', 'Necessary for fatty acid synthesis.'),
  ('B6', 'Helps your body release sugar from stored carbohydrates for energy and create red blood cells.'),
  ('B7', 'Plays a role in the metabolism of fatty acids, amino acids and glucose.'),
  ('B9', 'Important for proper cell division.'),
  ('B12', 'Necessary for red blood cell formation and proper nervous system and brain function.'),
  ('C', 'Required for the creation of neurotransmitters and collagen, the main protein in your skin.'),
  ('D', 'Promotes proper immune function and assists in calcium absorption and bone growth.'),
  ('E', 'Assists immune function and acts as an antioxidant that protects cells from damage.'),
  ('K', 'Required for blood clotting and proper bone development.'),
  )


# Create your models here.

class Vitamin(models.Model):
    name = models.CharField(
        max_length=5,
        choices=VITAMIN_TYPES
    )

    def __str__(self):
        return f'{self.get_name_display()}'

    def get_absolute_url(self):
        return reverse('vitamin_detail', kwargs={'pk': self.id})

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    vitamins = models.ManyToManyField(Vitamin)
    
    def __str__(self):
        return self.name

class Juice(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    drink_type = models.CharField(
        max_length=1,
        choices=DRINK_TYPES,
        default=DRINK_TYPES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fruits = models.ManyToManyField(Fruit)
    
    def __str__(self):
        return f'{self.name} {self.get_drink_type_display()}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    fav_juice = models.CharField(max_length=50)

    def __str__(self):
      return f'{self.first_name}'

