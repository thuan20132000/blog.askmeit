from django.db import models

# Create your models here.


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
        ('common','COMMON'),
    )

    name = models.CharField(max_length=100)
    phon_us = models.CharField(max_length=100)
    phon_uk = models.CharField(max_length=100)
    sound_us = models.CharField(max_length=255)
    sound_uk = models.CharField(max_length=255)
    definitions = models.JSONField(null=True, blank=True)

    certification_field =  models.CharField(choices=CERTIFICATION_CHOICES,max_length=10,default="common")

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

    def __str__(self):
        return self.name
