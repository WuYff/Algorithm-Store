# Generated by Django 2.0.12 on 2019-12-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0008_auto_20191208_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gkucun',
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gunit',
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(default='image/default.png', upload_to='df_goods/image/%Y/%m', verbose_name='图片路径'),
        ),
    ]
