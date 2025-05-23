# Generated by Django 3.2.25 on 2024-12-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20241213_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoschool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dat', models.DateField()),
                ('video', models.ImageField(null=True, upload_to='static/image/')),
                ('rem1', models.CharField(max_length=50, null=True)),
                ('rem2', models.CharField(max_length=50, null=True)),
                ('rem3', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mediaschool',
            name='video',
        ),
    ]
