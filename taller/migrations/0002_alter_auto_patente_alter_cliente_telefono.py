# Generated by Django 4.0.3 on 2022-03-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='patente',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
