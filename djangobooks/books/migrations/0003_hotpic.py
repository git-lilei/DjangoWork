# Generated by Django 2.2 on 2019-04-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190426_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='图片名称')),
                ('pic', models.ImageField(upload_to='hotpic', verbose_name='图片')),
                ('index', models.SmallIntegerField(unique=True, verbose_name='下标')),
            ],
            options={
                'verbose_name': '图片表',
                'verbose_name_plural': '图片表',
            },
        ),
    ]
