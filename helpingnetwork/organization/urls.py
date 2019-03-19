from django.urls import path,re_path
from . import views
import re

urlpatterns = [
    path('', views.signup,name='organization_signup'),
]
