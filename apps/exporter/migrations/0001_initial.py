# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('destination_type', models.SmallIntegerField(choices=[(0, 'Database'), (1, 'ECC System'), (2, 'CRM System')], default=0)),
                ('client', models.CharField(default='000', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exporter.Execution')),
            ],
        ),
        migrations.CreateModel(
            name='KB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('repository_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('kb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exporter.KB')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exporter.Project')),
            ],
        ),
        migrations.CreateModel(
            name='DatabaseDestination',
            fields=[
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exporter.Destination')),
                ('database_type', models.SmallIntegerField(choices=[(0, 'Microsoft SQL'), (1, 'MYSQL'), (2, 'Java Connector')], default=0)),
                ('host', models.CharField(blank=True, max_length=100)),
                ('port', models.CharField(blank=True, max_length=7)),
                ('database_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SAPDestination',
            fields=[
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exporter.Destination')),
                ('host', models.CharField(max_length=100)),
                ('sid', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='executionstep',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exporter.Step'),
        ),
        migrations.AddField(
            model_name='execution',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exporter.Project'),
        ),
    ]
