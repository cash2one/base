# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chinese', models.CharField(max_length=10)),
                ('math', models.CharField(max_length=10)),
                ('english', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('age', models.SmallIntegerField(default=b'0', verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84', choices=[(0, 18), (1, 19), (2, 20), (3, 21), (4, 22), (5, 23), (6, 24), (7, 25), (8, 26), (9, 27), (10, 28), (11, 29), (12, 30), (13, 31), (14, 32), (15, 33), (16, 34), (17, 35), (18, 36), (19, 37), (20, 38), (21, 39), (22, 40), (23, 41), (24, 42), (25, 43), (26, 44), (27, 45), (28, 46), (29, 47), (30, 48), (31, 49), (32, 50), (33, 51), (34, 52), (35, 53), (36, 54), (37, 55), (38, 56), (39, 57), (40, 58), (41, 59)])),
                ('gender', models.CharField(max_length=60, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'0', '\u7537'), (b'1', '\u5973')])),
                ('birth', models.DateField(default=b'1990-01-01', help_text=b'\xe5\x87\xba\xe7\x94\x9f\xe5\xb9\xb4\xe6\x9c\x88\xe6\x97\xa5', verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('phone', models.CharField(help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\xb8\xb8\xe7\x94\xa8\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', max_length=60, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')),
                ('email', models.EmailField(help_text=b'\xe8\xaf\xb7\xe5\x8a\xa1\xe5\xbf\x85\xe8\xbe\x93\xe5\x85\xa5', max_length=75, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe7\xae\xb1')),
                ('xl', models.CharField(max_length=60, verbose_name=b'\xe5\xad\xa6\xe5\x8e\x86', choices=[(b'0', b'\xe5\xa4\xa7\xe4\xb8\x93'), (b'1', b'\xe6\x9c\xac\xe7\xa7\x91'), (b'2', b'\xe7\xa1\x95\xe5\xa3\xab'), (b'3', b'\xe5\x8d\x9a\xe5\xa3\xab')])),
                ('graduatedfrom', models.CharField(help_text=b'\xe8\xbe\x93\xe5\x85\xa5\xe6\x82\xa8\xe7\x9a\x84\xe6\xaf\x95\xe4\xb8\x9a\xe5\xad\xa6\xe6\xa0\xa1\xe5\x90\x8d\xe7\xa7\xb0', max_length=60, verbose_name=b'\xe6\xaf\x95\xe4\xb8\x9a\xe9\x99\xa2\xe6\xa0\xa1')),
                ('marriage', models.CharField(max_length=60, verbose_name=b'\xe5\xa9\x9a\xe5\xa7\xbb\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'\xe5\xb7\xb2\xe5\xa9\x9a'), (b'1', b'\xe6\x9c\xaa\xe5\xa9\x9a')])),
                ('begin_date', models.DateField(default=b'2015-07-01', help_text=b'\xe4\xbd\x95\xe6\x97\xb6\xe5\xbc\x80\xe5\xa7\x8b\xe5\xad\xa6\xe4\xb9\xa0', verbose_name=b'\xe5\x85\xa5\xe5\xad\xa6\xe6\x97\xb6\xe9\x97\xb4')),
                ('courses', models.TextField(default=None, help_text=b'\xe5\xa4\x9a\xe9\x97\xa8\xe8\xaf\xbe\xe7\xa8\x8b\xe7\x94\xa8\xe2\x80\x9c|\xe2\x80\x9d\xe5\x88\x86\xe5\xbc\x80', max_length=254, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe8\xaf\xbe\xe7\xa8\x8b')),
                ('stay', models.BooleanField(default=True, help_text=b'\xe5\x8b\xbe\xe9\x80\x89\xe9\x80\x89\xe6\x8b\xa9\xe4\xbd\x8f\xe5\xae\xbf', verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbd\x8f\xe5\xae\xbf')),
                ('comefrom', models.CharField(default=b'\xe5\xa4\xa7\xe5\xad\xa6\xe6\xb8\xa0\xe9\x81\x93', max_length=60, verbose_name=b'\xe5\xad\xa6\xe5\x91\x98\xe6\x9d\xa5\xe6\xba\x90', choices=[(b'0', b'\xe6\x9c\x8b\xe5\x8f\x8b\xe4\xbb\x8b\xe7\xbb\x8d'), (b'1', b'\xe5\xa4\xa7\xe5\xad\xa6\xe6\xb8\xa0\xe9\x81\x93'), (b'2', b'\xe8\x87\xaa\xe5\xb7\xb1\xe4\xb8\x8a\xe9\x97\xa8'), (b'3', b'\xe7\x99\xbe\xe5\xba\xa6\xe6\x8e\xa8\xe5\xb9\xbf')])),
                ('import_phone', models.CharField(help_text=b'\xe4\xba\xb2\xe5\xb1\x9e\xe6\x88\x96\xe8\x80\x85\xe6\x9c\x8b\xe5\x8f\x8b\xe5\x8f\xaf\xe7\x94\xa8\xe7\x94\xb5\xe8\xaf\x9d', max_length=60, verbose_name=b'\xe7\xb4\xa7\xe6\x80\xa5\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba')),
                ('introducer', models.ForeignKey(verbose_name=b'\xe4\xbb\x8b\xe7\xbb\x8d\xe4\xba\xba', blank=True, to='students.Student', null=True)),
            ],
            options={
                'verbose_name': '\u5b66\u5458\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u5b66\u5458\u4fe1\u606f\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(to='students.Student'),
            preserve_default=True,
        ),
    ]
