from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # profile urls:
    path('profile/create/', views.profile_create, name='create profile'),
    path('profile/details/', views.profile_details, name='profile details'),
    path('profile/edit/', views.profile_edit, name='edit profile'),
    path('profile/delete/', views.profile_delete, name='delete profile'),
    # fruit urls:
    path('fruit/create/', views.fruit_create, name='create fruit'),
    path('fruit/details/<int:pk>/', views.FruitDetailsView.as_view(), name='fruit details'),
    path('fruit/edit/<int:pk>/', views.fruit_edit, name='edit fruit'),
    path('fruit/delete/<int:pk>/', views.fruit_delete, name='delete fruit'),
)