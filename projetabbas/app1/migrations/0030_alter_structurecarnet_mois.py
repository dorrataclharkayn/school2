# Generated by Django 3.2.25 on 2025-02-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_structurecarnet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structurecarnet',
            name='mois',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
