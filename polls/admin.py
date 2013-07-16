from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('poll','choice_text','vote')
	search_fields = ['choice_text','vote']
   
class PollAdmin(admin.ModelAdmin):
	list_display = ('question','pub_date',)
	search_fields = ['question']

 
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Poll,PollAdmin)
