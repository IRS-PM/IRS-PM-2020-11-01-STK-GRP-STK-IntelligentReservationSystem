# Generated by Django 3.1.2 on 2020-10-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nus', '0011_remove_establishments_days_in_advance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishments',
            name='sublocs',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
