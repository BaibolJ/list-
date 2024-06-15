from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginVi, name='login'),
    path('register/', regV, name='register'),
    path('index/', index, name='home'),
    path('course_detail/<int:course_id>/', course_detail, name='course_detail'),
    path('course_create/', course_create, name='create'),
    path('course_delete/<int:pk>/', course_delete, name='delete')
]


