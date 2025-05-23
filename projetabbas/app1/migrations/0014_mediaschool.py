# Generated by Django 3.2.25 on 2024-12-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20241208_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediaschool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dat', models.DateField()),
                ('image', models.ImageField(null=True, upload_to='static/image/')),
                ('video', models.FileField(null=True, upload_to='static/image/')),
                ('rem1', models.CharField(max_length=50)),
                ('rem2', models.CharField(max_length=50)),
            ],
        ),
    ]
