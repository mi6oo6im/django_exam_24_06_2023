from django.contrib import admin

# Register your models here.
from django_exam_24_06_2023.webapp.models import UserProfile, Fruit


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name']
