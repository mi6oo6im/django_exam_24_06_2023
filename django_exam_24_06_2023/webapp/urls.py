from django.urls import path
from . import views
from django.views.generic import DeleteView

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # profile urls:
    path('profile/create/', views.ProfileCreateView.as_view(), name='create profile'),
    path('profile/details/', views.ProfileDetailView.as_view(), name='profile details'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit profile'),
    path('profile/delete/', views.ProfileDeleteView.as_view(), name='delete profile'),
    # fruit urls:
    path('fruit/create/', views.CreateFruitView.as_view(), name='create fruit'),
    path('fruit/details/<int:pk>/', views.FruitDetailsView.as_view(), name='fruit details'),
    path('fruit/edit/<int:pk>/', views.EditFruitView.as_view(), name='edit fruit'),
    path('fruit/delete/<int:pk>/', views.fruit_delete, name='delete fruit'),
)