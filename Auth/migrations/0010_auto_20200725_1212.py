# Generated by Django 2.2.13 on 2020-07-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_auto_20200719_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Charter Date'),
        ),
        migrations.AddField(
            model_name='club',
            name='meetingPlace',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Meeting Place'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_club',
            field=models.BooleanField(default=False, verbose_name='Club status'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_rotaractor',
            field=models.BooleanField(default=False, verbose_name='Rotaractor'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Name'),
        ),
    ]