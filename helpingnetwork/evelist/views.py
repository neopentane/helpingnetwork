from django.shortcuts import render
from django.shortcuts import render,redirect
from organization.models import Organization
from .models import Event
from django.http import HttpResponse
# Create your views here.
def index(request):
    x=Event.objects.all()
    return render(request, 'evelist/index.html',{'x': x})

def desc(request, event_id):
    x=Event.objects.get(pk=event_id)
    y=x.description
    #return render(request,'evelist')    
    return HttpResponse("description: %s" % y)
