# Generated by Django 3.1.13 on 2021-11-19 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0026_investitionskosten_abgabesystem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investitionskosten',
            name='investitionskosten_Kw_Gewerk_Erzeugung2',
        ),
    ]
