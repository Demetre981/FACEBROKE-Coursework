# Generated by Django 4.2.4 on 2023-08-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_notification_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_picture',
            field=models.ImageField(default='timeline-1.jpg', upload_to='background_images'),
        ),
    ]
