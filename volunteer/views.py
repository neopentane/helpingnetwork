from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm,VolunteerRegisterForm
from .models import Volunteer,City
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from evelist.models import Event,Signup,EventImages
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		form2=VolunteerRegisterForm(request.POST)
		if form.is_valid() and form2.is_valid():
			new_user=form.save()
			new_volunteer=form2.save(commit=False)
			new_volunteer.user=new_user
			new_volunteer.save()		
	else:
			form = UserRegisterForm()
			form2=VolunteerRegisterForm(request.POST)
	return render(request, 'volunteer/register.html', {'form': form,'form2':form2})


@login_required
def profile(request):
	current_user = request.user
	try:
		v=current_user.volunteer
		e=Event.objects.filter(venue=v.my_city)
		context={
		"Events":e
		}
		return render(request,'volunteer/profile.html',context)
	except:
		return render(request,'organization/home.html')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
