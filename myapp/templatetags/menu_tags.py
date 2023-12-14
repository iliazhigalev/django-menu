from django import template
from myapp.models import MenuItem

register = template.Library()

@register.inclusion_tag('myapp/menu_template.html')
def draw_menu(menu_name):
    if menu_name!='all':
        menu_items = MenuItem.objects.get(url=menu_name)
    else:
        menu_items = MenuItem.objects.all()

    return {'menu_items': menu_items,}

