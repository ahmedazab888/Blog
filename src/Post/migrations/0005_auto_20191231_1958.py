# Generated by Django 2.2.7 on 2019-12-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20191231_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/default.png', upload_to='post_img/'),
        ),
    ]
