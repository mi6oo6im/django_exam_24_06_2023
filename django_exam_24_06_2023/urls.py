from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('django_exam_24_06_2023.webapp.urls')),
)
