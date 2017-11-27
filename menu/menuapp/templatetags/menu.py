from django import template

register = template.Library()

@register.inclusion_tag('menuapp/menu.html')
def draw_menu(menu_name):
    # TODO: load menu from models

    # TODO: here I just use dumb data to test whether my template works.
    menu = [
        {
            'title': 'level1',
            'link': 'http://www.example.com/level1',
            'indent': False,
            'dedent': False,
        },
        {
            'indent': True,
            'dedent': False,
        },
        {
            'title': 'level1-1',
            'link': 'http://www.example.com/level1-1',
            'indent': False,
            'dedent': False,
        },
        {
            'indent': False,
            'dedent': True,
        },
        {
            'title': 'level2',
            'link': 'http://www.example.com/level1',
            'indent': False,
            'dedent': False,
        },
    ]
    return {'menu': menu}