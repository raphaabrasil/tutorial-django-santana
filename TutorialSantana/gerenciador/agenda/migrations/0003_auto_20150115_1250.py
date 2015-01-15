# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20150115_1247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemAgendas',
            new_name='ItemAgenda',
        ),
    ]
