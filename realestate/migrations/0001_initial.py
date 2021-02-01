# Generated by Django 3.1.4 on 2021-02-01 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='upload/')),
                ('status', models.TextField(choices=[('pending', 'PENDING'), ('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='pending')),
            ],
        ),
        migrations.CreateModel(
            name='AdminRealestateCategory',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='realestate.category')),
            ],
            bases=('realestate.category',),
        ),
        migrations.CreateModel(
            name='Realestate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('province', models.JSONField()),
                ('district', models.JSONField()),
                ('subDistrict', models.JSONField()),
                ('status', models.TextField(choices=[('pending', 'PENDING'), ('draft', 'DRAFT'), ('published', 'PUBLISHED'), ('sold', 'SOLD'), ('invoiced', 'INVOICED')], default='pending')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realestate_category', to='realestate.category')),
            ],
        ),
    ]
