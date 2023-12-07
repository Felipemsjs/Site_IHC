# Generated by Django 3.1.4 on 2023-12-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0006_projeto_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='billable',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='billable_amount',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='billable_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='estimate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='estimate_seconds',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dados',
            name='non_billable_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dados',
            name='time_seconds',
            field=models.CharField(max_length=20),
        ),
    ]