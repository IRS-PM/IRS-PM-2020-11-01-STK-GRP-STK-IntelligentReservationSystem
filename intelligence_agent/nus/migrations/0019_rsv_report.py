# Generated by Django 3.1.2 on 2020-11-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nus', '0018_auto_20201103_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='rsv_report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.TextField(max_length=50)),
                ('establishment', models.TextField(max_length=50)),
                ('hourly', models.TextField(max_length=50)),
                ('utilization', models.TextField(max_length=50)),
                ('acceptance', models.TextField(max_length=50)),
                ('source', models.TextField(max_length=50)),
                ('period', models.TextField(max_length=50)),
            ],
        ),
    ]
