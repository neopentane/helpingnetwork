from django.shortcuts import render,redirect
from .forms import OrganizationRegisterForm
from .models import Organization
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = OrganizationRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			o_name = form.cleaned_data.get('name')
			o_desp= form.cleaned_data.get('disp')
			t_user=User.objects.filter(username=username).first()
			p=Organization(user=t_user,name=o_name,description=o_desp)
			p.save()
			messages.success(request, f'Account created for {username}!')
			return redirect('register')
	else:
			form = OrganizationRegisterForm()
	return render(request, 'organization/signup.html', {'form': form})

