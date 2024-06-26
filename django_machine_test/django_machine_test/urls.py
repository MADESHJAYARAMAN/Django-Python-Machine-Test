"""
URL configuration for django_machine_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django_machine_test/urls.py

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
    path('admin/', admin.site.urls),
    path('api/clients/', views.ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('api/clients/<int:pk>/', views.ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
    path('api/projects/', views.ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy'),
]
