# Generated by Django 3.0.3 on 2022-05-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '03'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_img',
            field=models.ImageField(upload_to='plantindex/plants/'),
        ),
    ]
