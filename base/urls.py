from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-employee/', views.createEmployee, name='create-employee'),
    path('create-job/', views.createJob, name='create-job'),
    path('delete-employee/<str:pk>', views.deleteEmployee, name='delete-employee'),
    path('update-employee/<str:pk>', views.updateEmployee, name='update-employee'),
    path('delete-job/<str:pk>', views.deleteJob, name='delete-job'),
    path('update-job/<str:pk>', views.updateJob, name='update-job'),
]