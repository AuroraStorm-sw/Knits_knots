# Generated by Django 3.2.21 on 2023-11-22 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20231110_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocall',
            name='booking_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
