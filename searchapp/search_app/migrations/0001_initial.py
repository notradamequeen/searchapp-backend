# Generated by Django 3.1.1 on 2020-09-22 05:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZztempCodinghw2Model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
            ],
            options={
                'db_table': 'zztemp_codinghw2',
            },
        )
    ]
