# Generated by Django 5.0.2 on 2024-05-11 06:45

import django.db.models.deletion
import src.er_card.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateTimeField(unique=True, verbose_name='Admission date')),
                ('delivery_time', models.DurationField(blank=True, null=True, verbose_name='Delivery time')),
                ('patient_condition', models.CharField(blank=True, choices=[('satisfactory', 'Satisfactory'), ('moderate', 'Moderate severity'), ('severe', 'Severe'), ('extremely_severe', 'Extremely severe')], max_length=30, null=True, verbose_name='Patient condition')),
                ('patient_complaints', models.TextField(blank=True, null=True, verbose_name='Patient complaints')),
                ('heart_stopped', models.BooleanField(default=False, verbose_name='Heart stopped')),
                ('hospitalization_date', models.DateField(verbose_name='Hospitalization date')),
                ('hospitalization_type', models.CharField(choices=[('planned', 'Planned'), ('urgent', 'Urgent'), ('emergency', 'Emergency')], max_length=15, verbose_name='Hospitalization type')),
                ('diagnosed_by', models.CharField(blank=True, choices=[('outpatient_facility', 'Outpatient facility'), ('ambulance_brigade', 'Ambulance brigade'), ('reception_department', 'Reception department'), ('inpatient_facility', 'Inpatient facility')], max_length=50, null=True, verbose_name='Diagnosed by')),
                ('additional_information', models.TextField(blank=True, null=True, verbose_name='Additional information')),
            ],
            options={
                'verbose_name': 'Admission data',
                'verbose_name_plural': 'Admission data',
            },
        ),
        migrations.CreateModel(
            name='Complication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.PositiveSmallIntegerField(choices=[(1, 'I complication group'), (2, 'II complication group'), (3, 'III complication group')], verbose_name='Group')),
                ('name', models.CharField(max_length=150, verbose_name='Complication')),
            ],
            options={
                'verbose_name': 'Complications group',
                'verbose_name_plural': 'Complications groups',
            },
        ),
        migrations.CreateModel(
            name='InternationalClassificationOfDiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True, verbose_name='Diagnosis code')),
                ('title', models.CharField(max_length=255, verbose_name='Diagnosis title')),
            ],
            options={
                'verbose_name': 'Diagnosis',
                'verbose_name_plural': 'Diagnoses',
            },
        ),
        migrations.CreateModel(
            name='AdmissionAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('attachment', models.FileField(max_length=255, upload_to=src.er_card.utils.get_file_path, verbose_name='Attachment')),
                ('admission_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='er_card.admissiondata', verbose_name='Electronic Rehabilitation Card')),
            ],
            options={
                'verbose_name': 'Admission attachment',
                'verbose_name_plural': 'Admission attachments',
            },
        ),
        migrations.CreateModel(
            name='ElectronicRehabilitationCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='er_cards', to='management.doctor', verbose_name='Created doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='er_cards', to='management.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Electronic rehabilitation card',
                'verbose_name_plural': 'Electronic rehabilitation cards',
            },
        ),
        migrations.AddField(
            model_name='admissiondata',
            name='er_card',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admission_data', to='er_card.electronicrehabilitationcard', verbose_name='Electronic rehabilitation card'),
        ),
        migrations.CreateModel(
            name='ERCardAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('attachment', models.FileField(max_length=255, upload_to=src.er_card.utils.get_file_path, verbose_name='Attachment')),
                ('er_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='er_card.electronicrehabilitationcard', verbose_name='Electronic Rehabilitation Card')),
            ],
            options={
                'verbose_name': 'ER Card attachment',
                'verbose_name_plural': 'ER Card attachments',
            },
        ),
        migrations.CreateModel(
            name='ConditionAssessmentSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morisky_green', models.PositiveSmallIntegerField(choices=[(1, 'Disaffected'), (2, 'Uncommitted'), (3, 'Under committed'), (4, 'Complaint')], verbose_name='Morisky Green')),
                ('examination_date', models.DateTimeField(verbose_name='Date of examination')),
                ('weight', models.FloatField(verbose_name='Weight')),
                ('height', models.FloatField(verbose_name='Height')),
                ('body_mass_index', models.FloatField(editable=False, verbose_name='Body mass index')),
                ('body_temperature', models.FloatField(verbose_name='Body temperature')),
                ('systolic_pressure', models.FloatField(verbose_name='Systolic blood pressure')),
                ('diastolic_pressure', models.FloatField(verbose_name='Diastolic blood pressure')),
                ('pulse_rate', models.FloatField(verbose_name='Radial artery pulse rate')),
                ('respiratory_rate', models.FloatField(blank=True, null=True, verbose_name='Respiratory rate')),
                ('spo2', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='SPO2')),
                ('moist_rales', models.BooleanField(blank=True, default=False, verbose_name='Lung moist rales')),
                ('lower_limb_edema', models.BooleanField(blank=True, default=False, verbose_name='Swelling of the lower limbs')),
                ('creatinine', models.FloatField(verbose_name='Serum creatinine')),
                ('troponin', models.FloatField(verbose_name='Troponin I')),
                ('coronary_insufficiency', models.PositiveSmallIntegerField(choices=[(1, 'Absent'), (2, 'Rare'), (3, 'Moderate'), (4, 'Frequent')], verbose_name='Coronary insufficiency')),
                ('killip', models.PositiveSmallIntegerField(choices=[(1, 'Normal'), (2, 'Slightly reduced'), (3, 'Anomalous'), (4, 'Severe deficiency')], verbose_name='AHF severity class according to the Killip classification')),
                ('nyha', models.PositiveSmallIntegerField(choices=[(1, 'Normal'), (2, 'Light'), (3, 'Anomalous'), (4, 'Severe')], verbose_name='Functional class according to NYHA classification')),
                ('st_segment_elevation', models.BooleanField(default=False, verbose_name='ST segment elevation')),
                ('t_wave_inversion', models.BooleanField(default=False, verbose_name='T wave inversion ')),
                ('ami_clinical_case', models.BooleanField(default=False, verbose_name='Clinical case of AMI')),
                ('ami_date', models.DateTimeField(blank=True, null=True, verbose_name='Date of AMI')),
                ('ami_localization', models.CharField(choices=[('anterior_wall', 'Anterior wall'), ('anterior_apical', 'Anterior-apical'), ('anterolateral', 'Anterolateral'), ('anterior_septal', 'Anterior septal'), ('diaphragmatic', 'Diaphragmatic'), ('inferolateral', 'Inferolateral'), ('inferoposterior', 'Inferoposterior'), ('inferobasal', 'Inferobasal'), ('apical_lateral', 'Apical-lateral'), ('basalolateral', 'Basal-lateral'), ('superolateral', 'Superolateral'), ('lateral', 'Lateral'), ('rear', 'Rear'), ('posterobasal', 'Posterobasal'), ('posterolateral', 'Posterolateral'), ('posteroseptal', 'Posteroseptal'), ('septal', 'Septal'), ('right_ventricle', 'Right ventricle')], max_length=150, verbose_name='Localization of AMI')),
                ('mi_type', models.CharField(choices=[('type_1', 'Spontaneous MI caused by rupture or erosion of the ASB'), ('type_2', 'Secondary myocardial infarction associated with decreased oxygen supply'), ('type_3', 'Sudden coronary death'), ('type_4a', 'MI associated with PCI'), ('type_4b', 'MI associated with stent thrombosis after PCI'), ('type_4c', 'MI associated with restenosis after PCI'), ('type_5', 'MI associated with coronary artery bypass grafting.')], max_length=150, verbose_name='Type of Miocardium Infarction')),
                ('myocardium_damage', models.PositiveSmallIntegerField(choices=[(1, 'Small-focal'), (2, 'Macrofocal nontransmural'), (3, 'Transmural circular')], verbose_name='Depth and extent of myocardial damage')),
                ('acs_characteristics', models.CharField(blank=True, choices=[('unstable_angina', 'Unstable angina'), ('mi_without_st', 'Myocardial Infarction without ST'), ('mi_with_st', 'Myocardial Infarction with ST'), ('mi_without_q_wave', 'Myocardial Infarction without Q wave'), ('mi_with_q_wave', 'Myocardial Infarction with Q wave')], max_length=150, verbose_name='Characteristics of ACS')),
                ('coronary_angiography', models.BooleanField(default=False, verbose_name='Coronary angiography')),
                ('stenting', models.BooleanField(default=False, verbose_name='Stenting')),
                ('revascularization', models.BooleanField(default=False, verbose_name='Revascularization')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Is complete')),
                ('coronary_lesion_degree', models.CharField(choices=[('single_vessel', 'Single vessel'), ('two_vessel', 'Two vessel'), ('multivessel', 'Multivessel')], max_length=50, verbose_name='Degree of the coronary lesion')),
                ('affected_vessel_name', models.CharField(choices=[('left_coronary_artery_trunk', 'Left coronary artery trunk'), ('anterior_descending_artery', 'Anterior descending artery'), ('diagonal_artery', 'Diagonal artery'), ('circumflex_artery', 'Circumflex artery'), ('blunt_edge_branch', 'Blunt edge branch'), ('septal_interventricular_branches', 'Septal interventricular branches'), ('intermediate_artery', 'Intermediate artery'), ('right_coronary_artery', 'Right coronary artery'), ('sharp_edge_branch', 'Sharp edge branch'), ('sinoatrial_node_artery', 'Sinoatrial node Artery'), ('posterior_interventricular_branch', 'Posterior interventricular branch')], max_length=50, null=True, verbose_name='Name of the affected vessel')),
                ('vessel_lesion_volume', models.FloatField(verbose_name='Vessel lesion volume')),
                ('index_syntax', models.FloatField(blank=True, null=True, verbose_name='Index SYNTAX')),
                ('issue_date', models.DateTimeField(verbose_name='Issue date')),
                ('accompanying_pathologies', models.BooleanField(default=False, verbose_name='Accompanying pathologies')),
                ('grace_score', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='GRACE score')),
                ('stemi', models.BooleanField(default=False, editable=False, verbose_name='is stemi')),
                ('lethality_hospital', models.CharField(editable=False, max_length=10, verbose_name='Lethality percent in hospital')),
                ('lethality_six_months', models.CharField(editable=False, max_length=10, verbose_name='Lethality percent in six months')),
                ('risk_hospital', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], editable=False, max_length=20, verbose_name='Lethality risk in hospital')),
                ('risk_six_months', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], editable=False, max_length=20, verbose_name='Lethality risk in six months')),
                ('patient_severity_class', models.PositiveSmallIntegerField(editable=False, verbose_name='Patient severity class')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('complications', models.ManyToManyField(blank=True, related_name='ca_sheets', to='er_card.complication', verbose_name='Complications')),
                ('er_card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ch_sheet', to='er_card.electronicrehabilitationcard', verbose_name='Electronic rehabilitation card')),
                ('accompanying_pathologies_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accompanying_pathologies', to='er_card.internationalclassificationofdiseases', verbose_name='Accompanying pathologies type')),
                ('primary_disease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clinical_diagnosis', to='er_card.internationalclassificationofdiseases', verbose_name='Primary disease')),
            ],
            options={
                'verbose_name': 'Condition assessment sheet',
                'verbose_name_plural': 'Condition assessment sheets',
            },
        ),
        migrations.AddField(
            model_name='admissiondata',
            name='preliminary_diagnosis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='er_cards', to='er_card.internationalclassificationofdiseases', verbose_name='Preliminary diagnosis'),
        ),
    ]
