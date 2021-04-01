from django.db import models

# Create your models here.


class Topic(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    image = models.ImageField(upload_to='upload/flashcard/', blank=True)

    status = models.TextField(
        max_length=22, choices=STATUS_CHOICES, default='published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self,):
        return "Topic: %s" % self.name


class VocabularyCard(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=255)
    word_type = models.CharField(max_length=255, null=True)
    phon_us = models.CharField(max_length=255, null=True)
    phon_uk = models.CharField(max_length=255, null=True)
    sound_us = models.FileField(
        upload_to='upload/flashcard/audio/', blank=True)
    sound_uk = models.FileField(
        upload_to='upload/flashcard/audio/', blank=True)
    meaning = models.CharField(max_length=255, null=True)
    definition = models.TextField(null=True)
    example = models.TextField(null=True)
    topics = models.ManyToManyField(Topic)
    status = models.TextField(
        max_length=22, choices=STATUS_CHOICES, default='published')

    def __str__(self,):
        return "VocabularyCard: %s " % self.name
