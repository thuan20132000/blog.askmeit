from django.db import models
import uuid

# Create your models here.

class ReadingTopic(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    image = models.ImageField(
        upload_to='upload/reading/', blank=True, null=True)

    status = models.TextField(
        max_length=22, choices=STATUS_CHOICES, default='published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self,):
        return "Topic: %s" % self.name


class ReadingPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('pending', 'Pending'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    image = models.ImageField(upload_to='upload/reading/', blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    summary = models.TextField(blank=True,null=True)
    practice_number = models.IntegerField(default=0)
    
    reading_topic = models.ForeignKey(
        ReadingTopic,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reading_topic"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    status = models.TextField(
        max_length=22, choices=STATUS_CHOICES, default='published')




class ReadingPostVocabulary(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    ID = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    word_type = models.CharField(max_length=255, null=True, blank=True)
    phon_us = models.CharField(max_length=255, null=True, blank=True)
    phon_uk = models.CharField(max_length=255, null=True, blank=True)
    sound_us = models.FileField(
        upload_to='readingpostvocabulary/audio', blank=True)
    sound_uk = models.FileField(
        upload_to='readingpostvocabulary/audio', blank=True)
    meaning = models.CharField(max_length=255, null=True, blank=True)
    definition = models.TextField(null=True, blank=True)
    example = models.TextField(null=True, blank=True)
    status = models.TextField(
        max_length=22, choices=STATUS_CHOICES, default='published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    reading_post = models.ForeignKey(
        ReadingPost,
        on_delete=models.CASCADE,
        related_name="reading_post",
        blank=True,
        null=True
    )

    def __str__(self,):
        return "VocabularyCard: %s " % self.name

   
    def get_only_name(self,):
        return self.name