from django.contrib import admin
from polls.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [('type of question', {'fields':['question'],"classes":['collapse']}),('date infos',{'fields':['pub_date'],"classes":['collapse']})]
class ChoiceAdmin(admin.ModelAdmin):
	fieldsets = [('No of votes',{'fields':['vote'],"classes":['collapse']}),('Your choice',{'fields':['choice_text'],"classes":['collapse']}), (None,{'fields':['poll']})]
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
