# Generated by Django 2.2.13 on 2020-07-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0013_auto_20200721_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event7',
            field=models.CharField(max_length=100, verbose_name='Instagram Link'),
        ),
        migrations.AlterField(
            model_name='report',
            name='bulletin02',
            field=models.CharField(max_length=100, verbose_name='Link'),
        ),
    ]
