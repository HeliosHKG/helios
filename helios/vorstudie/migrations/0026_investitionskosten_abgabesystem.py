# Generated by Django 3.1.13 on 2021-11-19 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0021_auto_20211118_2038'),
        ('vorstudie', '0025_auto_20211118_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='investitionskosten',
            name='abgabesystem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.abgabesystem_hlks'),
        ),
    ]