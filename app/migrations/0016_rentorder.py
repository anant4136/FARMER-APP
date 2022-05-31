# Generated by Django 3.2.9 on 2022-05-31 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_machine_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=30)),
                ('num_of_days', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.machine')),
            ],
        ),
    ]