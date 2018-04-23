from django.contrib import admin
from django.contrib.admin.models import LogEntry
from mptt.admin import MPTTModelAdmin


class FixedMPTTModelAdmin(MPTTModelAdmin):

    def __init__(self, *args, **kwargs):
        super(FixedMPTTModelAdmin, self).__init__(*args, **kwargs)
        mptt_opts = self.model._mptt_meta
        # Use mptt default ordering
        self.ordering = (mptt_opts.tree_id_attr, mptt_opts.left_attr)
        if self.list_display and self.sortable not in self.list_display:
            self.list_display = list(self.list_display) + [self.sortable]
        self.list_editable = self.list_editable or []
        if self.sortable not in self.list_editable:
            self.list_editable = list(self.list_editable) + [self.sortable]
        self.exclude = self.exclude or []
        if self.sortable not in self.exclude:
            self.exclude = list(self.exclude) + [self.sortable]

    # Return default admin ChangeList
    def get_changelist(self, request, **kwargs):
        return admin.views.main.ChangeList


@admin.register(LogEntry)
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
