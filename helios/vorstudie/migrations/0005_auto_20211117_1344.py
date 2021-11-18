# Generated by Django 3.1.13 on 2021-11-17 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0007_auto_20211117_1342'),
        ('vorstudie', '0004_leistung_technikflächen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technikflächen',
            name='projekt_spez',
        ),
        migrations.AddField(
            model_name='technikflächen',
            name='projekt_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.projekt'),
        ),
    ]