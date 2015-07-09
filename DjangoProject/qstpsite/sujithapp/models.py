from django.db import models
# Create your models here.

class figureofspeech(models.Model):
	figureofspeech_text = models.CharField(max_length = 250)
	
	def __unicode__(self):
		return self.figureofspeech_text
	
	class Meta: app_label = "sujithapp"

class language(models.Model):
	language_Country = models.CharField(max_length = 300)
	def __unicode__(self):
		return self.language_Country
		
	class Meta: 
		app_label = "sujithapp"