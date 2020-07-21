# Generated by Django 2.2.13 on 2020-07-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0006_bod_event_futureevent_gbm'),
    ]

    operations = [
        migrations.AddField(
            model_name='gbm',
            name='gbm5',
            field=models.CharField(default='', max_length=10, verbose_name='Attendance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gbm',
            name='gbm2',
            field=models.CharField(max_length=50, verbose_name='Agenda'),
        ),
    ]
