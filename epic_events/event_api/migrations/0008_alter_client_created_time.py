# Generated by Django 4.1.1 on 2022-10-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0007_alter_client_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]