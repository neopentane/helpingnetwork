from django.shortcuts import render,redirect
from .forms import OrganizationRegisterForm,CreateEventForm,AddImageForm,AddOrgImage
from .models import Organization,OrganizationImages
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
			o_vision= form.cleaned_data.get('vision')
			o_mission= form.cleaned_data.get('mission')
			o_link=form.cleaned_data.get('link')
			t_user=User.objects.filter(username=username).first()
			p=Organization(user=t_user,name=o_name,vision=o_vision,mission=o_mission,link=o_link)
			p.save()
			messages.success(request, f'Account created for {username}!')
			return redirect('register')
	else:
			form = OrganizationRegisterForm()
	return render(request, 'organization/signup.html', {'form': form})

def cenv(request):
	if request.method == 'POST':
		form1=CreateEventForm(request.POST,request.FILES)
		if form1.is_valid():
			new_event=form1.save(commit=False)
			new_event.organizer=request.user.organization
			new_event.save()
			return redirect('add_img')
	else:
		form1=CreateEventForm()
	return render(request, 'organization/cenv.html',{'form': form1})
def aenv(request):
	c_organization=request.user.organization
	allevents=Event.objects.filter(organizer=c_organization)
	context={
		"events":allevents
	}
	return render(request, 'organization/aenv.html',context)
def changep(request):
	if request.method == 'POST':
		form2=AddOrgImage(request.POST,request.FILES)
		if form2.is_valid():
			new_org=form2.save(commit=False)
			new_org.organization=request.user.organization
			new_org.save()
			return redirect('change_profile')
	else:
		form2=AddOrgImage()
	return render(request, 'organization/changep.html',{'form': form2})
def a_image(request):
	if request.method == 'POST':
		form2=AddImageForm(request.POST,request.FILES)
		if form2.is_valid():
			form2.save()
			return redirect('add_img')
	else:
		form2=AddImageForm()
	return render(request, 'organization/a_image.html',{'form': form2})

def printo(request):
	if request.method == 'GET':
		o_org=request.GET.get('org')
		org=Organization.objects.filter(name=o_org).first()
		images=OrganizationImages.objects.filter(organization=org)
		context={
			"name":org.name,
			"vision":org.vision,
			"mission":org.mission,
			"link":org.link,
			"img":images,

		}
	return render(request, 'organization/orgview.html',context)
