from django.db import models
from sujithapp.models import figureofspeech
 
class word(models.Model):
        
        language = models.ForeignKey(language)
        figureofspeech = models.ForeignKey(figureofspeech)
        word_text = models.CharField(max_length = 250)
        word_meaning = models.CharField(max_length = 300)
 
        def __unicode__(self):
                return self.word_text
class language(newmodel.Model):
        language_Country = newmodels.CharField(max_lenth = 300)
# Create your models here.
