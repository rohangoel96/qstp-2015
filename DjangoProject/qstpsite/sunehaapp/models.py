from django.db import models

class figureofspeech(models.Model):
	figureofspeech_text = models.CharField(max_length = 250)
	
	def __unicode__(self):
		return self.figureofspeech_text
		

class language(models.Model):
	language_Country = models.CharField(max_length = 300)
	def __unicode__(self):
		return self.language_Country
		
		
class word(models.Model):
        
        language = models.ForeignKey(language, null="TRUE")
        figureofspeech = models.ForeignKey(figureofspeech, null="TRUE")
        word_text = models.CharField(max_length = 250)
        word_meaning = models.CharField(max_length = 300)
 
        def __unicode__(self):
			return self.word_text
				
