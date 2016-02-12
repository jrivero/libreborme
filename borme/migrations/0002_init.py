# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_hstore.fields
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('borme', '0001_hstore_extension'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('id_anuncio', models.IntegerField()),
                ('year', models.IntegerField()),
                ('datos_registrales', models.CharField(max_length=70)),
                ('actos', django_hstore.fields.SerializedDictionaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Borme',
            fields=[
                ('cve', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('url', models.URLField(blank=True, null=True)),
                ('from_reg', models.IntegerField()),
                ('until_reg', models.IntegerField()),
                ('province', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=20)),
                ('anuncios', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=models.IntegerField())),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=260, db_index=True)),
                ('nif', models.CharField(max_length=10)),
                ('slug', models.CharField(max_length=260, serialize=False, primary_key=True)),
                ('date_creation', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('AEIE', 'Agrupación Europea de Interés Económico'), ('AIE', 'Agrupación de Interés Económico'), ('COOP', 'Cooperativa'), ('FP', 'Fondo de Pensiones'), ('SA', 'Sociedad Anónima'), ('SAD', 'Sociedad Anónima Deportiva'), ('SAL', 'Sociedad Anónima Laboral'), ('SAP', 'Sociedad Anónima P?'), ('SAS', 'Sociedad por Acciones Simplificada'), ('SAU', 'Sociedad Anónima Unipersonal'), ('SC', 'Sociedad Comanditaria'), ('SCP', 'Sociedad Civil Profesional'), ('SL', 'Sociedad Limitada'), ('SLL', 'Sociedad Limitada Laboral'), ('SLLP', 'Sociedad Limitada Laboral P?'), ('SLNE', 'Sociedad Limitada Nueva Empresa'), ('SLP', 'Sociedad Limitada Profesional'), ('SLU', 'Sociedad Limitada Unipersonal'), ('SRL', 'Sociedad de Responsabilidad Limitada'), ('SRLL', 'Sociedad de Responsabilidad Limitada Laboral'), ('SRLP', 'Sociedad de Responsabilidad Limitada Profesional')], max_length=50)),
                ('date_updated', models.DateField(db_index=True)),
                ('in_bormes', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
                ('anuncios', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=models.IntegerField())),
                ('cargos_actuales_p', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
                ('cargos_actuales_c', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
                ('cargos_historial_p', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
                ('cargos_historial_c', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField()),
                ('version', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('in_companies', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=models.CharField(max_length=260))),
                ('in_bormes', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
                ('date_updated', models.DateField(db_index=True)),
                ('cargos_actuales', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
                ('cargos_historial', django.contrib.postgres.fields.ArrayField(size=None, default=list, base_field=django_hstore.fields.DictionaryField())),
            ],
        ),
        migrations.CreateModel(
            name='BormeLog',
            fields=[
                ('borme', models.OneToOneField(to='borme.Borme', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_parsed', models.DateTimeField(blank=True, null=True)),
                ('parsed', models.BooleanField(default=False)),
                ('errors', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='borme',
            field=models.ForeignKey(to='borme.Borme'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='company',
            field=models.ForeignKey(to='borme.Company'),
        ),
        migrations.AlterIndexTogether(
            name='anuncio',
            index_together=set([('id_anuncio', 'year')]),
        ),
    ]
