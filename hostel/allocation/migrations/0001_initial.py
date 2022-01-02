# Generated by Django 3.2.9 on 2021-12-22 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hostel_Name', models.CharField(max_length=200)),
                ('Hostel_Type', models.CharField(max_length=200)),
                ('Hostel_Code', models.CharField(max_length=50)),
                ('Hall_Master', models.CharField(max_length=200)),
                ('Chief_Porter', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Hostel',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=100)),
                ('session_start', models.DateField()),
                ('session_end', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Session',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_number', models.CharField(max_length=100)),
                ('student_firstname', models.CharField(max_length=100)),
                ('student_lastname', models.CharField(max_length=100)),
                ('student_other_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('department', models.CharField(max_length=150)),
                ('level', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_Number', models.CharField(max_length=20)),
                ('Bed_Spaces', models.IntegerField()),
                ('IsFull', models.BooleanField(default=False)),
                ('Hostel_Located', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.hostel')),
            ],
            options={
                'verbose_name_plural': 'Room',
            },
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.hostel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.room')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.student')),
            ],
            options={
                'verbose_name_plural': 'Allocation',
            },
        ),
    ]