from django.shortcuts import render, redirect, reverse
# Imports for signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Needed for protecting the routes
from django.contrib.auth.decorators import login_required
from .models import Juice, Profile, Vitamin, Fruit
from .forms import JuiceForm, FruitForm, UserForm, ProfileForm, AddVitaminForm

from django.db import transaction


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
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    # else render a template with a form for the user to enter their info.
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# USER PROFILE
@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, 'registration/profile.html', context)

# UPDATE USER PROFILE

@login_required
@transaction.atomic
def profile_update(request):
    message =''
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            message = 'Profile successfully updated.'
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'message': message
    })

# DELETE USER PROFILE
@login_required
def profile_delete(request, user_id):
    if request.method == 'POST':
        print(f'deleting user {request.user}')
        User.objects.filter(pk=request.user.pk).update(is_active=False, email='')
        return redirect('logout')
    else:
        return redirect('/')

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
            # saving the many-to-many relationship - juice - fruits
            form.save_m2m()
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
@login_required
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
@login_required
def juice_delete(request, juice_id):
    Juice.objects.get(id=juice_id).delete()
    return redirect('juices_index')


# VIEW FRUIT DETAIL

@login_required
def fruits_detail(request, fruit_id): 
    fruit = Fruit.objects.get(id=fruit_id)
    vitamins_not_assoc = Vitamin.objects.exclude(id__in = fruit.vitamins.all().values_list('id'))

    vitamin_form = AddVitaminForm()
    vitamins = fruit.vitamins.all()
    return render(request, 'fruits/detail.html', {'fruit': fruit, 'vitamin_form': vitamin_form, 'vitamins': vitamins_not_assoc })

# ADD NEW FRUIT

@login_required
def new_fruit(request): 
    if request.method == 'POST':
        form = FruitForm(request.POST)
        # validate the form
        if form.is_valid():
            fruit = form.save(commit=False)
            fruit.save()
            return redirect('fruits_detail', fruit.id)
    else:
        form = FruitForm()
    context = {'form': form}
    return render(request, 'fruits/fruit_form.html', context)

# VIEW ALL FRUITS

@login_required
def fruits_index(request): 
    fruits = Fruit.objects.all()
    return render(request, 'fruits/index.html', { 'fruits': fruits })


# UPDATE FRUIT
@login_required
def fruits_update(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    if request.method == 'POST':
        form = FruitForm(request.POST, instance=fruit)
        fruit = form.save()
        return redirect('detail', fruit.id)
    else:
        form = FruitForm(instance=fruit)
    return render(request, 'fruits/fruit_form.html', { 'form': form })


# ADD VITAMIN

@login_required
def add_vitamin(request, fruit_id):
    form = AddVitaminForm(request.POST)
    vitamin = Vitamin.objects.get(id=request.POST['vitamins'][0])
    
    if form.is_valid():
        # makes the connection between fruit id and vitamin id
        Fruit.objects.get(id=fruit_id).vitamins.add(vitamin.id)
        
    return redirect('fruits_detail', fruit_id=fruit_id)
