# Generated by Django 3.1.13 on 2021-11-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0009_auto_20211117_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stammdaten_Technickzentralen_Elektro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leistung_pro_m2', models.FloatField()),
                ('Gebaudegroesse', models.FloatField()),
                ('zentraltyp', models.CharField(max_length=50)),
                ('zentralengroesse', models.FloatField()),
            ],
        ),
    ]
