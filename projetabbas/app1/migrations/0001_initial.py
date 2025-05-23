# Generated by Django 3.2.25 on 2024-11-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anne',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ida', models.CharField(max_length=20)),
                ('anne', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='login11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='logindirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='matiere',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('nommatiere', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('anne', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mony',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classe', models.CharField(max_length=50)),
                ('anne', models.CharField(max_length=50)),
                ('amountll', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amountdd', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='nstudent101',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=50)),
                ('nom', models.TextField(max_length=50)),
                ('pere', models.TextField(max_length=50)),
                ('famille', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='regeleve',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code1', models.CharField(max_length=50)),
                ('nom1', models.CharField(max_length=50)),
                ('pere1', models.CharField(max_length=50)),
                ('famille1', models.CharField(max_length=50)),
                ('anne1', models.CharField(max_length=50)),
                ('mois', models.CharField(max_length=50)),
                ('classe1', models.CharField(max_length=50)),
                ('section1', models.CharField(max_length=50)),
                ('math', models.DecimalField(decimal_places=2, max_digits=7)),
                ('physique', models.DecimalField(decimal_places=2, max_digits=7)),
                ('chimie', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('arab1', models.DecimalField(decimal_places=2, max_digits=7)),
                ('arab2', models.DecimalField(decimal_places=2, max_digits=7)),
                ('arab3', models.DecimalField(decimal_places=2, max_digits=7)),
                ('francais1', models.DecimalField(decimal_places=2, max_digits=7)),
                ('francais2', models.DecimalField(decimal_places=2, max_digits=7)),
                ('francais3', models.DecimalField(decimal_places=2, max_digits=7)),
                ('eng', models.DecimalField(decimal_places=2, max_digits=7)),
                ('civisme', models.DecimalField(decimal_places=2, max_digits=7)),
                ('historique', models.DecimalField(decimal_places=2, max_digits=7)),
                ('geographie', models.DecimalField(decimal_places=2, max_digits=7)),
                ('economie', models.DecimalField(decimal_places=2, max_digits=7)),
                ('socialite', models.DecimalField(decimal_places=2, max_digits=7)),
                ('philosophie', models.DecimalField(decimal_places=2, max_digits=7)),
                ('informatique', models.DecimalField(decimal_places=2, max_digits=7)),
                ('religieu', models.DecimalField(decimal_places=2, max_digits=7)),
                ('art', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sport', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pass1', models.DecimalField(decimal_places=2, max_digits=7)),
                ('som1', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('som2', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('numeducation', models.CharField(max_length=50)),
                ('directeur', models.CharField(max_length=50)),
                ('tasnif', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('tarhis', models.CharField(max_length=50)),
                ('mohafaza', models.CharField(max_length=50)),
                ('kdaa', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('rem1', models.CharField(max_length=50)),
                ('rem2', models.CharField(max_length=50)),
                ('num1', models.IntegerField(verbose_name='10')),
                ('num2', models.IntegerField(verbose_name='10')),
            ],
        ),
        migrations.CreateModel(
            name='stok',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('f1', models.CharField(max_length=50)),
                ('f2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='stok11',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temp', models.CharField(max_length=50)),
                ('anne', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student101',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('pere', models.CharField(max_length=50)),
                ('famille', models.CharField(max_length=50)),
                ('mere', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('lieu', models.CharField(max_length=50)),
                ('segel', models.CharField(max_length=50)),
                ('dat', models.DateField()),
                ('rem1', models.CharField(max_length=50)),
                ('rem2', models.CharField(max_length=50)),
                ('num1', models.IntegerField(verbose_name='10')),
                ('num2', models.IntegerField(verbose_name='10')),
                ('quit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='visamoy',
            fields=[
                ('visamoye', models.CharField(max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
