# Generated by Django 3.1.4 on 2021-04-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabularycard',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='vocabularycard',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='vocabularycard',
            name='sound_uk',
            field=models.FileField(blank=True, upload_to='upload/flashcard/audio/'),
        ),
        migrations.AlterField(
            model_name='vocabularycard',
            name='sound_us',
            field=models.FileField(blank=True, upload_to='upload/flashcard/audio/'),
        ),
        migrations.AlterField(
            model_name='vocabularycard',
            name='topics',
            field=models.ManyToManyField(to='flashcard.Topic'),
        ),
    ]
