# Generated by Django 3.1.4 on 2021-01-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vieclam24h', '0004_auto_20210128_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.TextField(choices=[('pending', 'PENDING'), ('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='pending'),
        ),
    ]
