# Generated by Django 3.2.21 on 2023-11-23 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_videocall_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocall',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='videocall',
            name='booking_time',
            field=models.TimeField(),
        ),
    ]
