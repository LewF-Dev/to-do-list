# Generated by Django 4.2.1 on 2024-08-13 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
