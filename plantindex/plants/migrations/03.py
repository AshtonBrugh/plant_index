# Generated by Django 3.0.3 on 2022-05-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '02'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]