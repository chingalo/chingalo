from django.contrib import admin
from polls.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [('type of question', {'fields':['question']}),('date infos',{'fields':['pub_date']})]
class ChoiceAdmin(admin.ModelAdmin):
	fieldsets = [('No of votes',{'fields':['vote']}),('Your choice',{'fields':['choice_text']}), (None,{'fields':['poll']})]
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
