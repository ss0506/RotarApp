# Generated by Django 2.2.13 on 2020-07-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_auto_20200719_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='clubCode',
            field=models.IntegerField(blank=True, verbose_name='Club Code'),
        ),
    ]