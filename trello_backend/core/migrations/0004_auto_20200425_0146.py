# Generated by Django 3.0.4 on 2020-04-24 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200424_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 1, 46, 47, 437754)),
        ),
    ]
