# Generated by Django 3.1.13 on 2021-11-18 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0013_auto_20211118_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abgabesystem_HLKS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abgabesystem', models.CharField(max_length=50)),
                ('gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk')),
            ],
        ),
        migrations.CreateModel(
            name='Energietraeger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energietraeger', models.CharField(max_length=50)),
                ('treibhausgasemission', models.FloatField()),
                ('nationaler_gew_faktor', models.FloatField()),
                ('gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk')),
            ],
        ),
        migrations.RenameField(
            model_name='nutzungsstammdaten_sia2024',
            old_name='energie_pro_m2_Klassifizierung_Gewerk2',
            new_name='energie_pro_m2_Klassefizierung_Gewerk2',
        ),
        migrations.RenameField(
            model_name='nutzungsstammdaten_sia2024',
            old_name='gewerk',
            new_name='gewerk2',
        ),
        migrations.RenameField(
            model_name='nutzungsstammdaten_sia2024',
            old_name='klassifizierung',
            new_name='klassefizierung',
        ),
        migrations.RenameField(
            model_name='nutzungsstammdaten_sia2024',
            old_name='leistung_pro_m2_Klassifizierung_Gewerk2',
            new_name='leistung_pro_m2_Klassefizierung_Gewerk2',
        ),
        migrations.RenameField(
            model_name='nutzungsstammdaten_sia2024',
            old_name='raumtemparatur',
            new_name='raumtemparatur_sommer',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_erzeugung',
            name='erzeugungstyp',
        ),
        migrations.RemoveField(
            model_name='stammdaten_technickzentralen_elektro',
            name='Gebaudegroesse',
        ),
        migrations.RemoveField(
            model_name='stammdaten_technickzentralen_elektro',
            name='leistung_pro_m2',
        ),
        migrations.AddField(
            model_name='kostenstammdaten_hlks_erzeugung',
            name='einheitspreis_pro_m3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='nutzungsstammdaten_sia2024',
            name='raumtemparatur_winter',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stammdaten_technickzentralen_elektro',
            name='gebaudegroesse_bis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stammdaten_technickzentralen_elektro',
            name='gebaudegroesse_von',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stammdaten_technickzentralen_elektro',
            name='leistung_pro_m2_bis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stammdaten_technickzentralen_elektro',
            name='leistung_pro_m2_von',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stammdaten_technickzentralen_elektro',
            name='zentralengroesse',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Umwandlung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umwandlung', models.CharField(max_length=50)),
                ('wirkungsgrad', models.IntegerField()),
                ('energietraeger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.energietraeger')),
                ('gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk')),
            ],
        ),
        migrations.CreateModel(
            name='Technikzentralstammdaten_HLKS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leistung_Pro_Gewerk_Therm_von', models.FloatField(null=True)),
                ('leistung_Pro_Gewerk_Therm_bis', models.FloatField(null=True)),
                ('luftmenge_von', models.FloatField(null=True)),
                ('luftmenge_bis', models.FloatField(null=True)),
                ('zentralentyp', models.CharField(max_length=50)),
                ('zentralengroesse', models.FloatField()),
                ('erzeugungstyp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.erzeugungstyp')),
                ('gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk')),
                ('umwandlung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.umwandlung')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Unterhaltsfaktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unterhaltsfaktor_Pro_Gewerk', models.FloatField()),
                ('gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Umwandlung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umwandlung_Pro_Gewerk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.umwandlung')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Klassifizierung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gewerk2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk2')),
                ('klassifizierung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.klassifizierung')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Energietraeger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energietraeger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.energietraeger')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Energiepreise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energiepreis_Pro_Energietraeger', models.FloatField()),
                ('energietraeger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.energietraeger')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Abgabesystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abgabesystem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.abgabesystem_hlks')),
                ('gebaudenutzung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gebaudenutzung')),
            ],
        ),
        migrations.AddField(
            model_name='kostenstammdaten_hlks_erzeugung',
            name='umwandlung',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.umwandlung'),
        ),
        migrations.AlterField(
            model_name='kostenstammdaten_hlks_abgabe',
            name='abgabesystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projekt.abgabesystem_hlks'),
        ),
    ]