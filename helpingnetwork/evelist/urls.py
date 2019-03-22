from django.urls import path,re_path
from . import views
from organization.models import Organization,Event
import re

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:event_id>/',views.desc,name='desc')
]
