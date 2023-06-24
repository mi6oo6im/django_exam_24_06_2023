from django.shortcuts import render, redirect
from django_exam_24_06_2023.webapp.models import Fruit, UserProfile
from .forms import CreateUserForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, EditUserForm


# Create your views here.


def index(request):
    return render(request, 'webapp/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, 'webapp/dashboard.html', context)


# profile views:
def profile_create(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'webapp/create-profile.html', context)


def profile_details(request):
    return render(request, 'webapp/details-profile.html')


def profile_edit(request):
    current_profile = UserProfile.objects.first()
    form = EditUserForm(request.POST or None, instance=current_profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
        'profile': current_profile
    }

    return render(request, 'webapp/edit-profile.html', context)


def profile_delete(request):
    current_profile = UserProfile.objects.first()
    all_fruits = Fruit.objects.all()
    if request.method == 'POST':
        current_profile.delete()
        all_fruits.delete()
        return redirect('index')

    return render(request, 'webapp/delete-profile.html')


# fruit views:
def fruit_create(request):
    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'webapp/create-fruit.html', context)


def fruit_details(request, pk):
    current_fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': current_fruit
    }

    return render(request, 'webapp/details-fruit.html', context)


def fruit_edit(request, pk):
    current_fruit = Fruit.objects.get(pk=pk)
    form = EditFruitForm(request.POST or None, instance=current_fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'current_fruit': current_fruit
    }

    return render(request, 'webapp/edit-fruit.html', context)


def fruit_delete(request, pk):
    current_fruit = Fruit.objects.get(pk=pk)
    form = DeleteFruitForm(request.POST or None, instance=current_fruit)
    if request.method == 'POST':
        current_fruit.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'current_fruit': current_fruit
    }

    return render(request, 'webapp/delete-fruit.html', context)
