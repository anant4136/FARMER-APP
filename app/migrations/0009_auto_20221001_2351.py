# Generated by Django 3.2.9 on 2022-10-01 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220921_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='rentorder',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
