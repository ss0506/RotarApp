# Generated by Django 2.2.13 on 2020-07-21 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0007_auto_20200721_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bod',
            options={'verbose_name': 'BOD', 'verbose_name_plural': 'BODs'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='futureevent',
            options={'verbose_name': 'Future Event', 'verbose_name_plural': 'Future Events'},
        ),
        migrations.AlterModelOptions(
            name='gbm',
            options={'verbose_name': 'GBM', 'verbose_name_plural': 'GBMs'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Report', 'verbose_name_plural': 'Reports'},
        ),
    ]
