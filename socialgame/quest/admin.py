# -*- coding: utf-8 -*-
from django.contrib import admin

from quest.models import Quest, QuestProgress

class QuestAdmin(admin.ModelAdmin):
    
    search_fields = ('name'),

class QuestProgressAdmin(admin.ModelAdmin):

    pass


admin.site.register(Quest, QuestAdmin)
admin.site.register(QuestProgress, QuestProgressAdmin)


