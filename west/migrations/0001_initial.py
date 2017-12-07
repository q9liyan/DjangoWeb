# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('nid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', max_length=30, editable=False)),
                ('email', models.EmailField(max_length=254, db_index=True)),
                ('memo', models.TextField()),
                ('img', models.ImageField(upload_to=b'upload')),
                ('gender', models.IntegerField(default=1, choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')])),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(blank=True, to='west.UserType', null=True),
        ),
    ]
