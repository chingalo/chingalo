from django.contrib import admin
from polls.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fields = ['question', 'pub_date']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
