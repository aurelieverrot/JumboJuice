from django.contrib import admin
# Import your models
from .models import Fruit, Smoothie, Vitamin

# Register your models here.
admin.site.register(Fruit)
admin.site.register(Smoothie)
admin.site.register(Vitamin)
