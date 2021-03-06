# Generated by Django 4.0.3 on 2022-04-29 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='no value', max_length=20)),
                ('password', models.CharField(default='no value', max_length=20)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isAdminVerified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('name', models.CharField(default='no value', max_length=40)),
                ('bio', models.CharField(default='no value', max_length=20)),
                ('gender', models.CharField(default='no value', max_length=20)),
                ('age', models.IntegerField(default=1)),
                ('address', models.CharField(default='no value', max_length=100)),
                ('mobileNum', models.IntegerField(default=1)),
                ('dob', models.IntegerField(default=1)),
                ('lockerNum', models.IntegerField(default=1)),
                ('reg_no', models.IntegerField(default=1)),
                ('membership_no', models.IntegerField(default=1)),
                ('package', models.CharField(default='no value', max_length=20)),
                ('startDate', models.IntegerField(default=1)),
                ('period', models.IntegerField(default=1)),
                ('endDate', models.IntegerField(default=1)),
                ('isApproved', models.BooleanField(default=False)),
                ('m_uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='muid', serialize=False, to='core.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='GymTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordDate', models.CharField(max_length=20)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('neck', models.IntegerField(default=0)),
                ('shoulder', models.IntegerField(default=0)),
                ('chest', models.IntegerField(default=0)),
                ('upperArm', models.IntegerField(default=0)),
                ('forearm', models.IntegerField(default=0)),
                ('upperAbdomen', models.IntegerField(default=0)),
                ('lowerAbdomen', models.IntegerField(default=0)),
                ('waist', models.IntegerField(default=0)),
                ('hips', models.IntegerField(default=0)),
                ('thighs', models.IntegerField(default=0)),
                ('calf', models.IntegerField(default=1)),
                ('g_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guid', to='core.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordDate', models.CharField(max_length=20)),
                ('profileName', models.CharField(default='no name', max_length=40)),
                ('a_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auid', to='core.authuser')),
            ],
        ),
    ]
