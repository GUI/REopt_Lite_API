# Generated by Django 2.2.10 on 2020-09-02 21:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reo', '0071_windmodel_year_one_curtailed_production_series_kw'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemodel',
            name='emissions_reduction_accounting_method',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='emissions_reduction_max_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='emissions_reduction_min_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='renewable_generation_accounting_method',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='renewable_generation_max_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='renewable_generation_min_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_emissions_reduction_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_nonscope_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_renewable_generation_kwh',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_renewable_generation_pct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope1_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='sitemodel',
            name='year_one_scope2_emissions_series_lb_C02',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), default=list, size=None),
        ),
    ]
