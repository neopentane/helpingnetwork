from django.urls import path,re_path
from . import views
import re

urlpatterns = [
    path('signup/', views.register,name='register'),
    path('profile/', views.profile,name='profile'),
]
