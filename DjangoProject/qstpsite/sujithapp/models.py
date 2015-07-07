from django.db import models

# Create your models here.
class word(models.Model):
	word_text = models.CharField(max_length = 250)
	word_language = models.Charfield(max_length = 250)
	
	def __unicode__(self):
		return self.word_text