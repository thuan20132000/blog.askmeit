from django.db import models

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
    content_vocabulary = models.JSONField(null=True,blank=True)
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
