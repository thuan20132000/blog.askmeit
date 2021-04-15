from django.contrib import admin

# Register your models here.

from .models import Topic, VocabularyCard, Field
from django.db import models
from django.forms import Textarea


@admin.register(Topic)
class AdminTopic(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'created_at', 'field')


@admin.register(VocabularyCard)
class AdminVocabularyCard(admin.ModelAdmin):

    list_filter = ('topics', 'status',)
    list_display = ['name', 'get_topics', 'word_type',
                    'meaning', 'definition', 'example','created_at']
    list_editable = ['meaning', 'definition', 'example', ]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 3,
                                  'cols': 40,
                                  'style': 'height: 3em;'})},
    }


@admin.register(Field)
class AdminField(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'created_at')
