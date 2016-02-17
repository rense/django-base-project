from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('site/_menu.html')
def show_menu(active=None):
    menu_items = []
    for _item in MenuItem.published.all():
        menu_item = {
            'title': _item.title,
            'url': _item.url,
            'target': _item.get_target_display(),
        }
        if _item.slug == active:
            menu_item['active'] = True
        menu_items.append(menu_item)

    return {'menu': menu_items}

