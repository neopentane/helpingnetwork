from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	fist_name=forms.CharField(required=True, label="First_Name")
	last_name=forms.CharField(required=True, label="Last_Name")
	email = forms.EmailField()
	city =forms.CharField(required=True, label="City_Name")

	class Meta:
		model = User
		fields = ['username','email','password1','password2','city','fist_name','last_name']
	'''def save(self, commit=True):
		user=super(UserCreationForm, self).save(commit=False)
		#user.first_name= self.cleaned_data["First_Name"]
		user.last_name = self.cleaned_data["Last_Name"]	
		user.last_name = self.cleaned_data["City_Name"]	
		if commit:
			user.save()
		return user
	'''
