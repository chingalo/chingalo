from django import forms
from polls.models import Poll, Choice
#definition of form for deals with poll
class Create_poll(forms.ModelForm):
	class Meta:
		model = Poll
		fields=('question',)
class Create_choice(forms.ModelForm):
	class Meta:
		model = Choice
		fields=('poll','choice_text',)
