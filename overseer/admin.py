# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Avaliation

admin.site.site_header = 'Overseer administration'

class AvaliationAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload', 'date')
    list_display_links = ('id',)
    list_per_page = 10

# Register your models here.
admin.site.register(Avaliation, AvaliationAdmin)
