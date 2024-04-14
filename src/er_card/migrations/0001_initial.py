# Generated by Django 5.0.2 on 2024-04-10 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicRehabilitationCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('admission_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='er_cards', to='management.admissiondata', verbose_name='Admission data')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='er_cards', to='management.doctor', verbose_name='Created doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Electronic rehabilitation card',
                'verbose_name_plural': 'Electronic rehabilitation cards',
            },
        ),
        migrations.CreateModel(
            name='AttachedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('file', models.FileField(upload_to='uploads/% Y/% m/% d/', verbose_name='File')),
                ('er_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='er_card.electronicrehabilitationcard', verbose_name='ER card')),
            ],
            options={
                'verbose_name': 'Attached file',
                'verbose_name_plural': 'Attached files',
            },
        ),
    ]
