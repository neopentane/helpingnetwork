from django.shortcuts import render,redirect
from organization.models import Organization,OrganizationImages
from .models import Event,EventImages,Signup
from django.http import HttpResponse
from .forms import EventSignupForm
# Create your views here.
def index(request):
    x=Event.objects.all()
    return render(request, 'evelist/index.html',{'x': x})

def desc(request, event_id):
    x=Event.objects.get(pk=event_id)
    y=x.description
    #return render(request,'evelist')
    return HttpResponse("description: %s" % y)


def printo(request):
	if request.method == 'GET':
		c_event=request.GET.get('event')
		c_org=request.GET.get('org')
		org=Organization.objects.filter(name=c_org).first()
		eventt=Event.objects.filter(name=c_event).first()
		images=EventImages.objects.filter(i_event=eventt)
		context={
         "event":c_event,
         "disp":eventt.description,
         "organizer":eventt.organizer,
         "venue":eventt.venue,
         "date":eventt.date,
         "org":c_org,
			"images":images
		}
	return render(request,'evelist/current_event.html',context)

def e_signin(request):
	if request.method == 'POST':
		form2=EventSignupForm(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('change_profile')
	else:
		form2=EventSignupForm()
	return render(request,'evelist/signin_event.html',{'form': form2})





