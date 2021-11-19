# Generated by Django 3.1.13 on 2021-11-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0023_auto_20211118_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investitionskosten',
            old_name='investitionskosten_m2_gewerk',
            new_name='investitionskosten_m2_elektro',
        ),
        migrations.AddField(
            model_name='investitionskosten',
            name='investitionskosten_m2_heizung',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investitionskosten',
            name='investitionskosten_m2_kaelte',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investitionskosten',
            name='investitionskosten_m2_lueftung',
            field=models.FloatField(blank=True, null=True),
        ),
    ]