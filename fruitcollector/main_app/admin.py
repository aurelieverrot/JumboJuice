from django.contrib import admin
# Import your models
from .models import Fruit, Juice, Vitamin, Profile

# Register your models here.
admin.site.register(Fruit)
admin.site.register(Juice)
admin.site.register(Vitamin)
admin.site.register(Profile)
