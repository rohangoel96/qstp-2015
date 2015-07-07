from django.db import models
from sunehaapp.models import language
# Create your models here.
class word(models.Model):
	word_text = models.CharField(max_length = 250)
	word_meaning = models.CharField(max_length = 250)
	language = models.ForeignKey(language)
	figureofspeech = models.ForeignKey(figureofspeech)
	
	def __unicode__(self):
		return self.word_text
		
class figureofspeech(models.Model):
	figureofspeech_text = models.CharField(max_length = 250)
	