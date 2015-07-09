from django.db import models

# Create your models here.

class LoginProfile(models.Model):
	username =  models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.username
	
	class Meta: 
		app_label = "rohanapp"
