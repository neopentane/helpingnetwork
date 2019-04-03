"""helpingnetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from organization import views as o_views
from django.conf import settings
from django.conf.urls.static import static
from evelist import views as e_views
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('evelist.urls'),),
    path('volunteer/', include('volunteer.urls'),),
    path('organization/', include('organization.urls' , namespace='organization'),),
	 path('login/', auth_views.LoginView.as_view(template_name='volunteer/login.html'), name='login'),
	 path('logout/', auth_views.LogoutView.as_view(template_name='volunteer/logout.html'), name='logout'),
	 path('c_event/', o_views.cenv, name='create_event'),
	 path('a_event/', o_views.aenv, name='all_event'),
	 path('c_profile/', o_views.changep, name='change_profile'),
	 path('add_img/', o_views.a_image, name='add_img'),
	 re_path(r'^view_organization/?$', o_views.printo, name='org_profile'),
	 re_path(r'^current_events/?$', e_views.printo, name='event_home'),
	 re_path(r'^signupnow/?$', e_views.e_signin, name='event_signin'),
]

if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
