# Generated by Django 3.1.2 on 2020-10-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nus', '0003_auto_20201012_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_register',
            name='business_contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='business_register',
            name='business_mail_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
