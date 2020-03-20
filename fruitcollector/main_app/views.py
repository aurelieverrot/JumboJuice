from django.shortcuts import render, redirect
# Imports for signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Needed for protecting the routes
from django.contrib.auth.decorators import login_required

from .models import Fruit
from .models import Vitamin
from .models import Smoothie
from .forms import SmoothieForm, FruitForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def fruits_index(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruits/index.html', { 'fruits': fruits})

@login_required
def fruits_detail(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    # gets the vitamins not associated with the fruit
    vitamins_nonrelated = Vitamin.objects.exclude(id__in = fruit.vitamins.all().values_list('id'))
    smoothie_form = SmoothieForm()
    return render(request, 'fruits/detail.html', {'fruit':fruit, 'smoothie_form': smoothie_form, 'vitamins': vitamins_nonrelated })

@login_required
def add_smoothie(request, fruit_id):
    form = SmoothieForm(request.POST)
    # validate the form
    if form.is_valid():
        new_smoothie = form.save(commit=False)
        new_smoothie.fruit_id = fruit_id
        new_smoothie.save()
    return redirect('detail', fruit_id=fruit_id)

@login_required
def assoc_vitamin(request, fruit_id, vitamin_id):
    Fruit.objects.get(id=fruit_id).vitamins.add(vitamin_id)
    return redirect('detail', fruit_id=fruit_id)

@login_required
def new_fruit(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            fruit = form.save(commit=False)
            fruit.user = request.user
            fruit.save()
            return redirect('detail', fruit.id)
    else:
        form = FruitForm()
    context = {'form': form}
    return render(request, 'fruits/fruit_form.html', context)

def signup(request):
    error_message=''
    # If user has submitted their info, the function should create the user and redirect.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # else render a template with a form for the user to enter their info.
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def fruits_update(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    if request.method == 'POST':
        form = FruitForm(request.POST, instance=fruit)
        fruit = form.save()
        return redirect('detail', fruit.id)
    else:
        form = FruitForm(instance=fruit)
    return render(request, 'fruits/fruit_form.html', { 'form': form})

def fruits_delete(request, fruit_id):
    Fruit.objects.get(id=fruit_id).delete()
    return redirect('index')