# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class SubsribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'from_page', 'time')
    search_fields = ('email',)
    ordering = ('time', )

admin.site.register(models.Subscribe, SubsribeAdmin)