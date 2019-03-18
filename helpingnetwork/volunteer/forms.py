from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Volunteer,City


class UserRegisterForm(UserCreationForm):
	first_name=forms.CharField(required=True, label="First_Name")
	last_name=forms.CharField(required=True, label="Last_Name")
	email = forms.EmailField()
	city =forms.CharField(required=True, label="City_Name")
	class Meta:
		model = User
		fields = ['username','email','password1','password2','city','first_name','last_name']
	def save(self,commit = True):
		user = super(UserRegisterForm, self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		
		if commit:
			user.save()
		return user
	
