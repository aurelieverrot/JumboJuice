from django.shortcuts import render, redirect
# Imports for signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Needed for protecting the routes
from django.contrib.auth.decorators import login_required

from .models import Fruit
from .models import Vitamin
from .models import Juice
from .forms import JuiceForm, FruitForm


# Create your views here.

# HOMEPAGE

def home(request):
    return render(request, 'home.html')

# ABOUT

def about(request):
    return render(request, 'about.html')

# SIGNUP

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

# VIEW ALL JUICES

@login_required
def juices_index(request): 
    juices = Juice.objects.all()
    return render(request, 'juices/index.html', { 'juices': juices} )

# CREATE NEW JUICE

@login_required
def new_juice(request):
    if request.method == 'POST':
        form = JuiceForm(request.POST)
        if form.is_valid():
            juice = form.save(commit=False)
            juice.user = request.user
            juice.save()
            return redirect('juice_detail', juice.id)
    else:
        form = JuiceForm()
    context = {'form': form}
    return render(request, 'juices/juice_form.html', context)

# VIEW JUICE DETAIL

@login_required
def juice_detail(request, juice_id):
    juice = Juice.objects.get(id=juice_id)
    # gets the vitamins not associated with the fruit
    # vitamins_nonrelated = Vitamin.objects.exclude(id__in = fruit.vitamins.all().values_list('id'))
    juice_form = JuiceForm()
    return render(request, 'juices/detail.html', {'juice':juice, 'juice_form': juice_form })

# JUICE UPDATE

def juice_update(request, juice_id):
    juice = Juice.objects.get(id=juice_id)
    if request.method == 'POST':
        form = JuiceForm(request.POST, instance=juice)
        juice = form.save()
        return redirect('juice_detail', juice.id)
    else:
        form = JuiceForm(instance=juice)
    return render(request, 'juices/juice_form.html', { 'form': form})

# JUICE DELETE

def juice_delete(request, juice_id):
    Juice.objects.get(id=juice_id).delete()
    return redirect('juices_index')


#------------------------------ OTHER

# 
@login_required
def fruits_detail(request, fruit_id): 
    fruit = Fruit.objects.get(id=fruit_id)
    # gets the vitamins not associated with the fruit
    vitamins_nonrelated = Vitamin.objects.exclude(id__in = fruit.vitamins.all().values_list('id'))
    juice_form = JuiceForm()
    return render(request, 'fruits/detail.html', {'fruit': fruit, 'juice_form': juice_form, 'vitamins': vitamins_nonrelated })

# form works
@login_required
def new_fruit(request): 
    if request.method == 'POST':
        form = FruitForm(request.POST)
        # validate the form
        if form.is_valid():
            fruit = form.save(commit=False)
            # fruit.juice = request.fruit
            fruit.save()
            return redirect('fruits_detail', fruit.id)
    else:
        form = FruitForm()
    context = {'form': form}
    return render(request, 'fruits/fruit_form.html', context)

# works
@login_required
def fruits_index(request): 
    fruits = Fruit.objects.all()
    return render(request, 'fruits/index.html', { 'fruits': fruits })


@login_required
def assoc_vitamin(request, fruit_id, vitamin_id):
    Fruit.objects.get(id=fruit_id).vitamins.add(vitamin_id)
    return redirect('detail', fruit_id=fruit_id)

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