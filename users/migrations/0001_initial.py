# Generated by Django 2.2.6 on 2020-07-28 11:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, default='', max_length=16)),
                ('last_name', models.CharField(blank=True, default='', max_length=16)),
                ('age', models.IntegerField(blank=True, default='1')),
                ('role', models.IntegerField(choices=[(1, 'farmer'), (2, 'ado'), (3, 'block_admin'), (4, 'dda'), (5, 'state_admin'), (6, 'super_admin')])),
                ('phone_number', models.CharField(blank=True, default='', max_length=10)),
                ('address', models.CharField(blank=True, default='', max_length=128)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdoReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_longitude', models.CharField(blank=True, default='', max_length=200)),
                ('report_latitude', models.CharField(blank=True, default='', max_length=100)),
                ('kila_num', models.CharField(blank=True, default='', max_length=50)),
                ('murrabba_num', models.CharField(blank=True, default='', max_length=50)),
                ('incident_reason', models.CharField(blank=True, default='', max_length=500)),
                ('remarks', models.CharField(blank=True, default='', max_length=500)),
                ('amount', models.CharField(blank=True, default='', max_length=500)),
                ('ownership', models.CharField(blank=True, default='', max_length=50)),
                ('action', models.CharField(blank=True, choices=[('chalaan', 'Challan'), ('FIR', 'FIR')], default='FIR', max_length=50)),
                ('fir', models.BooleanField(blank=True, default=False)),
                ('challan', models.BooleanField(blank=True, default=False)),
                ('flag', models.CharField(blank=True, choices=[('start', 'Start'), ('stop', 'Stop')], default='', max_length=50)),
                ('fire', models.CharField(blank=True, choices=[('fire', 'Fire'), ('nofire', 'No Fire')], default='', max_length=30)),
                ('created_on_ado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=200)),
            ],
            options={
                'get_latest_by': 'version',
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(blank=True, max_length=500)),
                ('block_code', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CompareData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('harsac_file', models.FileField(upload_to=users.models.path_file_name)),
                ('modis_file', models.FileField(upload_to=users.models.path_file_name_one)),
                ('viirs_npp1_file', models.FileField(upload_to=users.models.path_file_name_two)),
                ('viirs_noaa_file', models.FileField(upload_to=users.models.path_file_name_three)),
            ],
        ),
        migrations.CreateModel(
            name='dda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, max_length=500, unique=True)),
                ('district_code', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Email not valid', regex='^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$')])),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=500, unique=True)),
                ('state_code', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.CharField(blank=True, max_length=500)),
                ('village_code', models.CharField(blank=True, max_length=200)),
                ('village_subcode', models.CharField(blank=True, max_length=200)),
                ('ado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_ado', to='users.ado')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='village_block', to='users.Block')),
            ],
        ),
        migrations.CreateModel(
            name='super_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='state_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('acq_date', models.DateField(default=django.utils.timezone.now)),
                ('acq_time', models.TimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('ongoing', 'ongoing'), ('completed', 'completed')], default='pending', max_length=10)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('ado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_ado', to='users.ado')),
                ('dda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_dda', to='users.dda')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_district', to='users.District')),
                ('village_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_village', to='users.Village')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.AdoReport')),
            ],
        ),
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsidies', models.CharField(blank=True, max_length=64)),
                ('farmer_code', models.CharField(blank=True, max_length=64)),
                ('fathers_name', models.CharField(blank=True, max_length=64)),
                ('farmer_code_status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_state', to='users.State'),
        ),
        migrations.AddField(
            model_name='dda',
            name='district',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dda_district', to='users.District'),
        ),
        migrations.AddField(
            model_name='dda',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Email not valid', regex='^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$')])),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dc_district', to='users.District')),
            ],
        ),
        migrations.CreateModel(
            name='block_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Block')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_district', to='users.District'),
        ),
        migrations.AddField(
            model_name='adoreport',
            name='farmer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_farmer', to='users.farmer'),
        ),
        migrations.AddField(
            model_name='adoreport',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
    ]
