from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Volunteer,City
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			cityy=form.cleaned_data['city']
			cittyy=City.objects.filter(name=cityy).first()
			t_user=User.objects.filter(username=username).first()
			p=Volunteer(user=t_user,my_city=cittyy)
			p.save()
			messages.success(request, f'Account created for {username}!')
			return redirect('register')
	else:
			form = UserRegisterForm()
	return render(request, 'volunteer/register.html', {'form': form})


@login_required
def profile(request):
	current_user = request.user
	try:
		current_user.volunteer
		return render(request,'volunteer/profile.html')
	except:
		return render(request,'volunteer/testt.html')
