from .models import Signup
from django import forms

class EventSignupForm(forms.ModelForm):
	class Meta:
		model=Signup
		fields=["event","volunteer","invite_reason"]
