from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Organization,OrganizationImages
from evelist.models import Event,EventImages


class OrganizationRegisterForm(UserCreationForm):
	name=forms.CharField(required=True, label="Organization Name")
	email = forms.EmailField()
	vision = forms.CharField(max_length=200, widget=forms.TextInput({}),label="Vision")
	mission = forms.CharField(max_length=200, widget=forms.TextInput({}),label="Mission")
	link=forms.CharField(required=True, label="Link")
	class Meta:
		model = User
		fields = ['username','email','password1','password2','name','vision','mission','link']

class OrganizationUpdate(forms.ModelForm):
	class Meta:
		model=Organization
		fields = ['name']

'''
class CreateEventForm(forms.Form):
	name=forms.CharField(required=True, label="Event Name")
	description = forms.CharField(max_length=200, widget=forms.TextInput({}),label="description")
	venue=forms.CharField(required=True, label="Venue")
	date=forms.DateField(widget=forms.SelectDateWidget())
'''
class CreateEventForm(forms.ModelForm):
	class Meta:
		model=Event
		labels={"name":"Event Name","description":"Add Description","eventprofileImage":"Add Event Image"}
		fields=['name','description','venue','date','eventprofileImage']
		exclude=['organizer']

class AddOrgImage(forms.ModelForm):
	class Meta:
		model=OrganizationImages
		fields=['image']
		exclude=['organization']

class AddImageForm(forms.ModelForm):
	class Meta:
		model=EventImages
		fields=['i_event','image']
