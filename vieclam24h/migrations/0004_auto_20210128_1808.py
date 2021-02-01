# Generated by Django 3.1.4 on 2021-01-28 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vieclam24h', '0003_adminjob_jobcollaborator'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminJobCollaborator',
            fields=[
                ('jobcollaborator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vieclam24h.jobcollaborator')),
            ],
            bases=('vieclam24h.jobcollaborator',),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[('pending', 'PENDING'), ('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='pending'),
        ),
    ]
