from django.contrib import admin

# Register your models here.

from .models import ReadingTopic, ReadingPost
from django.db import models
from django.forms import Textarea
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


@admin.register(ReadingTopic)
class AdminReadingTopic(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'created_at',)


@admin.register(ReadingPost)
class AdminReadingPost(admin.ModelAdmin):
    list_filter = ('reading_topic', 'status',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 3,
                                  'cols': 40,
                                  'style': 'height: 3em;'})},
    }

    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }
