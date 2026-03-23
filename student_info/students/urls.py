from django.urls import path
from .views import student_create, student_success

urlpatterns = [
    path('new/', student_create, name='student_create'),
    path('success/', student_success, name='student_success'),
]