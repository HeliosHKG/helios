# Generated by Django 3.1.13 on 2021-11-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0009_auto_20211117_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='technikflaechen',
            name='leistung_pro_gewerk',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technikflaechen',
            name='luftwechsel',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technikflaechen',
            name='stammdaten_technikzentrale_elektro',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technikflaechen',
            name='stammdaten_technikzentrale_hlks',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
    ]
