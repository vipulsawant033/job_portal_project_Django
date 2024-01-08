# accounts/urls.py
from django.urls import path
from .views import CustomLoginView
import job_portal_project
from jobs import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
     path('accounts/logout/', LogoutView.as_view(), name='logout'),

]
