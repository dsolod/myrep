# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date_time', models.DateTimeField(verbose_name=b'date published')),
                ('pub_date', models.DateTimeField(verbose_name=b'date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='What',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('what_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Where',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('where_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Who',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('who_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='list',
            name='type_name',
            field=models.ManyToManyField(related_name='type', null=True, to='list.Type1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='what_name',
            field=models.ManyToManyField(related_name='what', null=True, to='list.What', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='where_name',
            field=models.ManyToManyField(related_name='where', null=True, to='list.Where', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='who_name',
            field=models.ManyToManyField(related_name='who', null=True, to='list.Who', blank=True),
            preserve_default=True,
        ),
    ]
