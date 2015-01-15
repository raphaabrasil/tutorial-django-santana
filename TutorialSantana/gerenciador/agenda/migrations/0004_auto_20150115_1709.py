# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0003_auto_20150115_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemagenda',
            name='participantes',
            field=models.ManyToManyField(related_name='item_participantes', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemagenda',
            name='usuario',
            field=models.ForeignKey(default=int, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
