# Generated by Django 4.2.4 on 2023-08-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_notification_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(default=None, max_length=100),
        ),
    ]