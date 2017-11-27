# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_editable = ('title',
        'link',
        'parent',
        'menu_name',
        'order_weight',
    )
    list_display_links = ('title_indented', )
    list_display = ('title_indented', 'title', 'link', 'parent', 'menu_name', 'order_weight')
    list_filter = ('menu_name', )


admin.site.register(MenuItem, MenuAdmin)