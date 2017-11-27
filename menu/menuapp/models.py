# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True)
    menu_name = models.CharField(max_length=30)
    order_weight = models.IntegerField()

    @property
    def title_indented(self):
        return '|----' * self.depth + self.title
    
    @property
    def depth(self):
        __depth = 0
        parent = self.parent
        while parent is not None:
            __depth += 1
            parent = parent.parent
        return __depth

    def __unicode__(self):
        return self.title
