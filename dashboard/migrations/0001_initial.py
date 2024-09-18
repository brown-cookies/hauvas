# Generated by Django 5.1.1 on 2024-09-18 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('code', models.CharField(max_length=6)),
                ('codename', models.CharField(max_length=20)),
                ('about', models.TextField(default='This is about course, populate it later')),
                ('syllabus', models.TextField(default='This is syllabus course, populate it later')),
                ('unit', models.IntegerField()),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('days', models.CharField(choices=[('MTH', 'Monday and Thursday'), ('TF', 'Tuesday and Friday'), ('WS', 'Wednesday and Saturday'), ('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday'), ('D', 'Default')], default='D', max_length=20)),
                ('room', models.CharField(default='undecided', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.block')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='main.department')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester', to='main.semester')),
            ],
            options={
                'permissions': [('change_about', 'Can change the about course'), ('change_syllabus', 'Can change the syllabus of the course')],
            },
        ),
        migrations.CreateModel(
            name='ModuleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Week-', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='dashboard.course')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Lesson 01', max_length=254)),
                ('short_description', models.CharField(default='Learn the {your explanation about the course}!', max_length=254)),
                ('description', models.TextField(default='Put your description here about the module, and even content')),
                ('content_url', models.CharField(default='none', max_length=255)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='dashboard.modulelist')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateTimeField()),
                ('academic_rank', models.CharField(choices=[('Professor', 'Professor'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Full Professor', 'Full Professor')], default='Professor', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professors', to='main.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='dashboard.professor'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=254)),
                ('year', models.IntegerField()),
                ('academic_status', models.CharField(choices=[('Active', 'Active'), ('On leave', 'On leave'), ('Suspended', 'Suspended'), ('Excused', 'Excused')], default='Active', max_length=254)),
                ('is_graduated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='main.block')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='main.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField()),
                ('completion_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Withdrawn', 'Withdrawn'), ('Dropped', 'Dropped')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='dashboard.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='main.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='dashboard.student')),
            ],
        ),
    ]
