from django.contrib import admin

from .models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_code', 'response_time', 'run_timedate')

admin.site.register(Poll, PollAdmin)