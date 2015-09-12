from django.contrib import admin
from django.contrib.admin.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin):
    """ Create an admin view of the history/log table
    """
    list_display = (
        'action_time',
        'user',
        'content_type',
        'change_message',
        'is_addition',
        'is_change',
        'is_deletion'
    )
    list_filter = ['content_type']
    ordering = ('-action_time',)

    date_hierarchy = 'action_time'

    readonly_fields = [
        'user',
        'content_type',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


admin.site.register(LogEntry, LogEntryAdmin)
