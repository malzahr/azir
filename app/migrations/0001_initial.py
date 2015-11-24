# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='module_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module_name', models.CharField(max_length=20)),
                ('module_caption', models.CharField(max_length=255)),
                ('module_extend', models.FileField(max_length=2000, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='server_app_categ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_categ_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='server_func_categ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_categ_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='server_list',
            fields=[
                ('server_name', models.CharField(max_length=13)),
                ('server_eip', models.CharField(max_length=15, blank=True)),
                ('server_ip', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('server_op', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
