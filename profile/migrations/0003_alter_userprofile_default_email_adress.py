# Generated by Django 3.2.21 on 2023-11-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20231124_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_email_adress',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]