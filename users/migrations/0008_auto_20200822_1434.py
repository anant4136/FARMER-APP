# Generated by Django 2.2.6 on 2020-08-22 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_adoreport_khasra_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state_admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='StateAdminUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
