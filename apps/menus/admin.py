from suit.admin import SortableModelAdmin
from django.contrib import admin

from apps.main.admin import FixedMPTTModelAdmin
from apps.menus.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(FixedMPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    sortable = 'sort_order'
    list_display = ('title', 'url', 'is_published')


