from django.db import models
from django.contrib.auth.models import User
from volunteer.models import City,Volunteer
from django.utils import timezone
from PIL import Image

class Organization(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	vision=models.TextField()
	mission=models.TextField()
	link=models.CharField(max_length=100)
	def __str__(self):
		return self.name



class OrganizationImages(models.Model):
	organization=models.ForeignKey(Organization, on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg', upload_to='organizationimages')
	#def __str__(self):
	#	return organization
