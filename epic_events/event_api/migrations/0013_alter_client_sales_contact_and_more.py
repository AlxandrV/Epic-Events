# Generated by Django 4.1.1 on 2022-10-08 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0012_alter_contract_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_api.salesteam'),
        ),
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_api.supportteam'),
        ),
    ]