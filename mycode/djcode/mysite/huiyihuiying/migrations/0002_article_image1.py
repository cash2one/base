# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('huiyihuiying', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image1',
            field=django_thumbs.db.models.ImageWithThumbsField(upload_to=b'uploads', blank=True),
            preserve_default=True,
        ),
    ]
