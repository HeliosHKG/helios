# Generated by Django 3.1.13 on 2021-11-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0012_auto_20211117_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leistung',
            name='flaeche_pro_Personenanzahl_Klassifizierung',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='leistung',
            name='leistung_pro_m2_Klassifizierung_Gewerk2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='leistung',
            name='luftwechsel_pro_Person_Klassifizierung',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='leistung',
            name='raumtemparatur_Klassifizierung',
            field=models.FloatField(null=True),
        ),
    ]
