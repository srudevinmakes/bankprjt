from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('application/',views.application,name='application'),
    path('application_submitted/',views.application_submitted,name='application_submitted'),
    path('home/', views.home, name='home'),

    # Add other URL patterns as needed
]
