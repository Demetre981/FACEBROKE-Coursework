# Generated by Django 4.2.4 on 2023-08-23 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_notification_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='type',
            new_name='record',
        ),
    ]
