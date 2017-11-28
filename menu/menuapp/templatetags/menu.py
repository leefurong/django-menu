from django import template
from menuapp.models import MenuItem
from __menu_parser import StructuredMenu

register = template.Library()

@register.inclusion_tag('menuapp/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    '''Notice: only absolute path is supported'''
    sm = StructuredMenu(menu_name, context.request.get_full_path())
    return {
                'menu': sm.get_normalized(),
                'menu_name': menu_name,
            }