from django.db import models
from sujithapp.models import *
class word(models.Model):
	language = models.ForeignKey(language, null="TRUE")
	figureofspeech = models.ForeignKey(figureofspeech, null="TRUE")
	word_text = models.CharField(max_length = 250)
	word_meaning = models.CharField(max_length = 300)
	def __unicode__(self):
		return self.word_text
	class Meta: 
		app_label = "sunehaapp"