# Generated by Django 3.1.13 on 2021-11-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0016_auto_20211118_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umwandlung',
            name='energietraeger',
        ),
        migrations.AddField(
            model_name='umwandlung',
            name='energietraeger',
            field=models.ManyToManyField(null=True, to='projekt.Energietraeger'),
        ),
    ]
