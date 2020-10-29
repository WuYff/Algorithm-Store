# Generated by Django 3.0.2 on 2020-01-17 00:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0012_auto_20200116_1159'),
        ('df_user', '0013_auto_20200116_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercreatetask',
            name='task_status',
        ),
        migrations.AddField(
            model_name='usercreatetask',
            name='algorithm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercreatetask',
            name='status',
            field=models.CharField(default='NOT_STARTED', max_length=20, verbose_name='任务状态'),
        ),
        migrations.AlterField(
            model_name='usercreatetask',
            name='last_update',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='算法状态更新时间'),
        ),
    ]