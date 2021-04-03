from django.contrib import admin

# Register your models here.

from .models import Vocabulary,Topic


@admin.register(Vocabulary)
class AdminVocabulary(admin.ModelAdmin):
    search_fields  = ['name']
    list_filter = ('topic','status',)
    list_display = ['name','created_at','topic']



@admin.register(Topic)
class AdminTopic(admin.ModelAdmin):
    search_fields = ['name']