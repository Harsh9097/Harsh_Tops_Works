"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
      path('', views.home, name='home'),
      path('add-student/', views.add_student, name='add-student'),
      path('all-student/', views.all_student, name='all-student'),
      path('search-student/', views.search_student, name='search-student'),
      path('del-student/<int:pk>/', views.del_student, name='del-student'),
      path('update-student/<int:id>/', views.update_student, name='update-student'),
      path('change-student/', views.change_student, name='change-student'),
      
]
