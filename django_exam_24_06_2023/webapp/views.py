from django.contrib.auth.models import User
from django.contrib.messages import success
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django_exam_24_06_2023.webapp.models import Fruit, UserProfile
from .forms import CreateUserForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, EditUserForm


# Create your views here.


def index(request):
    return render(request, 'webapp/index.html')


class DashboardView(ListView):
    model = Fruit
    template_name = "webapp/dashboard.html"


# old dashboard view:
# def dashboard(request):
#     fruits = Fruit.objects.all()
#     context = {
#         'fruits': fruits
#     }
#     return render(request, 'webapp/dashboard.html', context)

# profile views:

class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = CreateUserForm
    template_name = "webapp/create-profile.html"
    success_url = reverse_lazy('dashboard')


# old create profile view:
# def profile_create(request):
#     form = CreateUserForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'webapp/create-profile.html', context)


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'webapp/details-profile.html'

    def get_object(self, queryset=None):
        return UserProfile.objects.first()


# old profile details view:
# def profile_details(request):
#     return render(request, 'webapp/details-profile.html')


class ProfileEditView(UpdateView):
    model = UserProfile
    form_class = EditUserForm
    template_name = 'webapp/edit-profile.html'
    success_url = reverse_lazy('profile details')

    def get_object(self, queryset=None):
        return UserProfile.objects.first()


# old profile edit view:
# def profile_edit(request):
#     current_profile = UserProfile.objects.first()
#     form = EditUserForm(request.POST or None, instance=current_profile)
#     if form.is_valid():
#         form.save()
#         return redirect('profile details')
#
#     context = {
#         'form': form,
#         'profile': current_profile
#     }
#
#     return render(request, 'webapp/edit-profile.html', context)

class ProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = 'webapp/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return UserProfile.objects.first()

# old profile delete
# def profile_delete(request):
#     current_profile = UserProfile.objects.first()
#     all_fruits = Fruit.objects.all()
#     if request.method == 'POST':
#         current_profile.delete()
#         all_fruits.delete()
#         return redirect('index')
#
#     return render(request, 'webapp/delete-profile.html')


# fruit views:

class CreateFruitView(CreateView):
    model = Fruit
    template_name = 'webapp/create-fruit.html'
    form_class = CreateFruitForm
    success_url = reverse_lazy('dashboard')


# old create fruit view:
# def fruit_create(request):
#     form = CreateFruitForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'webapp/create-fruit.html', context)


class FruitDetailsView(DetailView):
    model = Fruit
    template_name = 'webapp/details-fruit.html'


# old fruit details view:
# def fruit_details(request, pk):
#     current_fruit = Fruit.objects.get(pk=pk)
#     context = {
#         'fruit': current_fruit
#     }
#
#     return render(request, 'webapp/details-fruit.html', context)

class EditFruitView(UpdateView):
    model = Fruit
    template_name = 'webapp/edit-fruit.html'
    success_url = reverse_lazy('dashboard')
    form_class = EditFruitForm


# old edit fruit view:
# def fruit_edit(request, pk):
#     current_fruit = Fruit.objects.get(pk=pk)
#     form = EditFruitForm(request.POST or None, instance=current_fruit)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         'form': form,
#         'current_fruit': current_fruit
#     }
#
#     return render(request, 'webapp/edit-fruit.html', context)


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
