# Generated by Django 3.1.13 on 2021-11-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0020_auto_20211118_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projektspezifikationen',
            name='projekt_gewerk',
        ),
        migrations.AddField(
            model_name='projektspezifikationen',
            name='projekt_gewerk',
            field=models.ManyToManyField(null=True, to='projekt.Gewerk'),
        ),
    ]