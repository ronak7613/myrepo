# Generated by Django 3.2 on 2023-11-07 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20231107_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table_swadhyay',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='table_swadhyay',
            name='off_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
    ]
