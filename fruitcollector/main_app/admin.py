from django.contrib import admin
# Import your models
from .models import Fruit, Juice, Vitamin

# Register your models here.
admin.site.register(Fruit)
admin.site.register(Juice)
admin.site.register(Vitamin)
