# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('keywords', models.CharField(max_length=80, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('author', models.CharField(max_length=30, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', blank=True)),
                ('date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('click', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\xac\xa1\xe6\x95\xb0')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe6\x96\x87\xe6\xa1\xa3\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': '\u6587\u6863\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sort', models.SmallIntegerField(default=50, help_text=b'\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7\xe6\x8e\x92\xe5\x88\x97', verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('fid', models.ForeignKey(blank=True, to='huiyihuiying.Channel', help_text=b'\xe4\xb8\x8d\xe9\x80\x89\xe4\xbb\xa3\xe8\xa1\xa8\xe7\x9a\x84\xe6\x98\xaf\xe9\xa1\xb6\xe7\xba\xa7\xe6\xa0\x8f\xe7\x9b\xae', null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe6\xa0\x8f\xe7\x9b\xae')),
            ],
            options={
                'verbose_name': '\u680f\u76ee\u7ba1\u7406',
                'verbose_name_plural': '\u680f\u76ee\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\xa0\x8f\xe7\x9b\xae', to='huiyihuiying.Channel'),
            preserve_default=True,
        ),
    ]
