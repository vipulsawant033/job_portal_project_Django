# jobs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/new/', views.job_new, name='job_new'),
    path('job/<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('job/<int:pk>/delete/', views.job_delete, name='job_delete'),
]
