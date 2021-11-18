# Generated by Django 3.1.13 on 2021-11-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0008_auto_20211117_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='kostenstammdaten_hlks_abgabe',
            name='einheitspreis_pro_m2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kostenstammdaten_hlks_erzeugung',
            name='einheitspreis_pro_KW',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kostenstammdaten_elektro',
            name='einheitspreis_pro_m2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutzungsstammdaten_sia2024',
            name='beleuchtungsstaerke',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutzungsstammdaten_sia2024',
            name='energie_pro_m2_Klassifizierung_Gewerk2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutzungsstammdaten_sia2024',
            name='flaeche_Pro_Personenanzahl',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutzungsstammdaten_sia2024',
            name='leistung_pro_m2_Klassifizierung_Gewerk2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutzungsstammdaten_sia2024',
            name='luftwechsel_Pro_Person',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutzungsstammdaten_sia2024',
            name='raumtemparatur',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projektspezifikationen',
            name='projekt_raumflaeche',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projektspezifikationen',
            name='projekt_raumhoehe',
            field=models.FloatField(blank=True, null=True),
        ),
    ]