from django.shortcuts import render,redirect
from .forms import OrganizationRegisterForm,CreateEventForm,AddImageForm
from .models import Organization
from django.contrib.auth.models import User
from django.contrib import messages
from evelist.models import Event,EventImages
from volunteer.models import City
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

def cenv(request):
	if request.method == 'POST':
		form1=CreateEventForm(request.POST)
		if form1.is_valid():
			e_name=form1.cleaned_data.get('name')
			e_description=form1.cleaned_data.get('description')
			cityy=form1.cleaned_data.get('venue')
			e_venue=City.objects.filter(name=cityy).first()			
			e_date=form1.cleaned_data.get('date')
			e_user=User.objects.filter(username=request.user).first()
			e_organizer=e_user.organization
			new_event=Event(name=e_name,venue=e_venue,date=e_date,description=e_description,organizer=e_organizer)
			new_event.save()
			return redirect('add_img')
	else:
		form1=CreateEventForm()
	return render(request, 'organization/cenv.html',{'form': form1})
def aenv(request):
	return render(request, 'organization/aenv.html')
def changep(request):
	return render(request, 'organization/changep.html')
def a_image(request):
	if request.method == 'POST':
		form2=AddImageForm(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('add_img')
	else:
		form2=AddImageForm()
	return render(request, 'organization/a_image.html',{'form': form2})

