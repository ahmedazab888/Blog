# Generated by Django 2.2.7 on 2019-12-31 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 31, 19, 23, 55, 934158)),
        ),
    ]
