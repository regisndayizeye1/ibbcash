# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0004_auto_20170606_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfert',
            name='statut',
            field=models.CharField(choices=[('ENVOYE', 'ENVOYE'), ('RECU', 'RECU')], default='ENVOYE', max_length=12),
        ),
        migrations.AlterField(
            model_name='transfert',
            name='MTCN',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Code du Client'),
        ),
        migrations.AlterField(
            model_name='transfert',
            name='first_namereceiver',
            field=models.CharField(max_length=50, verbose_name='Prenom du destinataire'),
        ),
    ]