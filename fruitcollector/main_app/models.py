from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

DRINK_TYPES = (
    ('G', 'Greens'),
    ('D', 'Detox'),
    ('S', 'Sweet')
)

# Create your models here.

class Vitamin(models.Model):
    name = models.CharField(max_length=10)
    health_benefits = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vitamin_detail', kwargs={'pk': self.id})

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
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

