from django.db import models

# Create your models here.
import uuid


class Language(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('pending', 'Pending'),
    )
    name = models.CharField(max_length=255)
    status = models.TextField(
        max_length=16, choices=STATUS_CHOICES, default='published')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('pending', 'Pending'),
    )
    name = models.CharField(max_length=255)
    status = models.TextField(
        max_length=16, choices=STATUS_CHOICES, default='published')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vocabulary(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('pending', 'Pending'),
    )
    CERTIFICATION_CHOICES = (
        ('ielts', 'IELTS'),
        ('toeic', 'TOEIC'),
        ('toefl', 'TOEFL'),
        ('common', 'COMMON'),
    )
    ID = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    word_type = models.CharField(max_length=100, null=True)
    phon_us = models.CharField(max_length=100, null=True)
    phon_uk = models.CharField(max_length=100, null=True)
    sound_us = models.FileField(upload_to='audio/', blank=True)
    sound_uk = models.FileField(upload_to='audio/', blank=True)
    definitions = models.JSONField(null=True, blank=True)

    certification_field = models.CharField(
        choices=CERTIFICATION_CHOICES, max_length=10, default="common")

    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        related_name="topic",
        null=True
    )

    status = models.TextField(
        max_length=16, choices=STATUS_CHOICES, default='published')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self,):
        return f"Name: {self.name}"
