# Generated by Django 2.2.13 on 2020-07-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0011_auto_20200721_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='month',
            field=models.CharField(max_length=10, verbose_name='Month'),
        ),
    ]