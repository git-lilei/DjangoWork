# Generated by Django 2.2 on 2019-04-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190425_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
    ]