# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipa.InstitutionType')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('bandwidth', models.PositiveIntegerField()),
                ('ipa_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipa.ParticipantInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='site_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipa.SiteType'),
        ),
    ]
