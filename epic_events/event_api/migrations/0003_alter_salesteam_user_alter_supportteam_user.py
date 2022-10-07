# Generated by Django 4.1.1 on 2022-10-02 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_api', '0002_alter_manageteam_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesteam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='supportteam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_api.manageteam', unique=True),
        ),
    ]