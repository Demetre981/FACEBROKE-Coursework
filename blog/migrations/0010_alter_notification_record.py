# Generated by Django 4.2.4 on 2023-08-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_type_notification_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='record',
            field=models.CharField(default='type', max_length=100),
        ),
    ]
