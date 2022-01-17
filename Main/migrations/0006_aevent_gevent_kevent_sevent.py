# Generated by Django 3.2.6 on 2021-09-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_extcevent_instruevent_itevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'AEvent',
            },
        ),
        migrations.CreateModel(
            name='GEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'GEvent',
            },
        ),
        migrations.CreateModel(
            name='KEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'KEvent',
            },
        ),
        migrations.CreateModel(
            name='SEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'SEvent',
            },
        ),
    ]
