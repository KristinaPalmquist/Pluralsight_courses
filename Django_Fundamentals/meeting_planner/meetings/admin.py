from django.contrib import admin
from django.contrib.admin import ModelAdmin
from meetings.models import Meeting, Room

# Register your models here.
admin.site.register(Room)


# admin.site.register(Meeting)
@admin.register(Meeting)
class MeetingAdmin(ModelAdmin):
    model = Meeting
    list_display = ('id', 'title', 'date', 'start_time', 'room')
    ordering = ('date', 'start_time')
    search_fields = ('title',)
