from django.contrib import admin

# Register your models here.

from .models import Topic,VocabularyCard,Field



@admin.register(Topic)
class AdminTopic(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ('name','created_at')



@admin.register(VocabularyCard)
class AdminVocabularyCard(admin.ModelAdmin):
    
    list_filter = ('topics','status',)


@admin.register(Field)
class AdminField(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ('name','created_at')