from django.urls import path,re_path
from . import views
import re
app_name = 'organization'
urlpatterns = [
    path('signup/', views.signup,name='organization_signup'),
]
