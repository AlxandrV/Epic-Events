# Generated by Django 4.1.1 on 2022-10-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0005_client_company_name_alter_manageteam_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company_name',
            field=models.CharField(max_length=250),
        ),
    ]
