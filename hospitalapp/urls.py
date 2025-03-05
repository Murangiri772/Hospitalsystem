
from django.contrib import admin
from django.urls import path
from hospitalapp import views
from hospitalapp import models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),

    path('delete/<int:id>', views.delete),
     path('view/', views.view, name='view'),
     path('delete/<int:id>', views.delete),

    path('edite/<int:id>', views.edite,name = 'edite'),
    path('viewedit/<int:id>', views.viewedit,name = 'viewedit'),
    path('', views.register,name = 'register'),
    path('login', views.login_view,name = 'login'),

]
