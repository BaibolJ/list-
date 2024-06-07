from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginVi, name='login'),
    path('register/', regV, name='register'),
    path('index/', index)
]


