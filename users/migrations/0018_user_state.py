# Generated by Django 2.2.6 on 2020-09-05 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200904_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_state', to='users.State'),
        ),
    ]