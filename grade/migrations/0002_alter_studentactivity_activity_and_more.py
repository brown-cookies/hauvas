# Generated by Django 5.1.1 on 2024-10-09 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentactivity',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='grade.activity'),
        ),
        migrations.AlterField(
            model_name='studentexam',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='grade.exam'),
        ),
    ]
