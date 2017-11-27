from django import template
from menuapp.models import MenuItem
from __menu_parser import StructuredMenu

register = template.Library()

@register.inclusion_tag('menuapp/menu.html')
def draw_menu(menu_name):
    sm = StructuredMenu(menu_name)
    return {
                'menu': sm.get_normalized(),
                'menu_name': menu_name,
            }