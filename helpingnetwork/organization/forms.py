from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Organization
from evelist.models import Event


class OrganizationRegisterForm(UserCreationForm):
	name=forms.CharField(required=True, label="Organization Name")
	email = forms.EmailField()
	disp = forms.CharField(max_length=200, widget=forms.TextInput({}),label="description")
	class Meta:
		model = User
		fields = ['username','email','password1','password2','name','disp']

class OrganizationUpdate(forms.ModelForm):	
	class Meta:
		model=Organization		
		fields = ['name']

class CreateEventForm(forms.Form):
	name=forms.CharField(required=True, label="Event Name")
	description = forms.CharField(max_length=200, widget=forms.TextInput({}),label="description")
	venue=forms.CharField(required=True, label="Venue")
	date=forms.DateField(widget=forms.SelectDateWidget())
	
