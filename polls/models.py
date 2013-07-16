from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
	
	
	
class Choice(models.Model):
	poll = models.ForeignKey(Poll)#to relate Poll and Choice classes
	choice_text = models.CharField(max_length=200)
	vote = models.IntegerField(default=0)#set initial value of vote to be zero
	def __unicode__(self):
		return self.choice_text
	
