# Generated by Django 3.2.21 on 2023-11-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20231026_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='products.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Tag name'),
        ),
    ]
