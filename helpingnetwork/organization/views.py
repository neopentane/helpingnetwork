from django.shortcuts import render

# Create your views here.

def signup(request):
	return render(request, 'volunteer/signup.html', {'form': "ASdjhasj"})
