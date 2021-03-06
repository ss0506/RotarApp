# Generated by Django 2.2.13 on 2020-08-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0020_auto_20200805_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bod',
            name='bod2',
            field=models.CharField(max_length=700, verbose_name='Agenda'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event1',
            field=models.CharField(max_length=35, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event6',
            field=models.CharField(max_length=700, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='futureevent',
            name='futureEvent1',
            field=models.CharField(max_length=35, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='futureevent',
            name='futureEvent2',
            field=models.CharField(max_length=700, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='gbm',
            name='gbm2',
            field=models.CharField(max_length=700, verbose_name='Agenda'),
        ),
        migrations.AlterField(
            model_name='report',
            name='bulletin00',
            field=models.CharField(max_length=35, verbose_name='Name of Bulletin'),
        ),
    ]
