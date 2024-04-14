# Generated by Django 5.0.2 on 2024-04-13 10:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_sheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraceScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acs_type', models.CharField(choices=[('stemi', 'ST-Elevation Myocardial Infarction'), ('nstemi', 'No ST-Elevation Myocardial Infarction')], max_length=10, verbose_name='Acute Coronary Syndrome Type')),
                ('lethality_type', models.CharField(choices=[('in_hospital', 'In hospital'), ('six_months', 'Within six months')], max_length=20, verbose_name='Lethality type')),
                ('score_range_start', models.PositiveIntegerField(blank=True, null=True, verbose_name='Score range start')),
                ('score_range_end', models.PositiveIntegerField(blank=True, null=True, verbose_name='Score range end')),
                ('risk', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=15, verbose_name='Risk')),
                ('lethality', models.FloatField()),
            ],
            options={
                'verbose_name': 'GRACE Scale',
                'verbose_name_plural': 'GRACE Scale',
            },
        ),
        migrations.AlterModelOptions(
            name='myocardialnecrosisbiochemicalmarker',
            options={'verbose_name': 'Myocardial necrosis biochemical marker', 'verbose_name_plural': 'Myocardial necrosis biochemical markers'},
        ),
        migrations.AddField(
            model_name='clinicaldiagnosis',
            name='ca_sheet',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='clinical_diagnosis', to='ca_sheet.conditionassessmentsheet', verbose_name='Condition Assessment sheet'),
            preserve_default=False,
        ),
    ]