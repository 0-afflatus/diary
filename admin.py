from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'title', 'owner', 'is_public', 'date_updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['start_date', 'title', 'details']
    readonly_fields = ('date_created', 'date_updated')

admin.site.register(Event, EventAdmin)