# Generated by Django 3.1.13 on 2021-11-17 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vorstudie', '0006_technikflächen_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technikflächen',
            old_name='name',
            new_name='name_technik',
        ),
    ]
