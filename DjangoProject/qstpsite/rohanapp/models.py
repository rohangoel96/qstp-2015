from django.db import models

# Create your models here.

class LoginProfile(models.Model):
	username =  models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.username
	
	class Meta: 
		app_label = "rohanapp"

class UserProfile(models.Model):
	username =  models.ForeignKey(LoginProfile, null="FALSE")
	name =  models.CharField(max_length = 50)
	email =  models.EmailField()
	phone_number = models.IntegerField()
	last_logged_in = models.DateTimeField()

	def __unicode__(self):
		return self.name
	
	class Meta: 
		app_label = "rohanapp"



		