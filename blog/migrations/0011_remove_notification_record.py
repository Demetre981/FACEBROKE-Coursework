# Generated by Django 4.2.4 on 2023-08-23 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_notification_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='record',
        ),
    ]
