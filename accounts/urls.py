# accounts/urls.py
from django.urls import path
from .views import CustomLoginView
import job_portal_project
from jobs import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),

]
