from django.contrib import admin

# Register your models here.

from .models import ReadingTopic, ReadingPost,ReadingPostVocabulary
from django.db import models
from django.forms import Textarea
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


@admin.register(ReadingTopic)
class AdminReadingTopic(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'created_at',)






class ReadingPostVocabularyTabularInline(admin.TabularInline):
    model = ReadingPostVocabulary
    fields = ['name','meaning','definition','example']

@admin.register(ReadingPost)
class AdminReadingPost(admin.ModelAdmin):
    list_filter = ('reading_topic', 'status',)
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title','content','created_at','reading_topic']
    
    list_editable = ['content',]

    inlines = [ReadingPostVocabularyTabularInline]
    
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 2,
                                  'cols': 40,
                                  'style': 'height: 3em;'})},
    }

    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }
