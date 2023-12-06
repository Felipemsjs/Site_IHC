# Generated by Django 3.1.4 on 2023-12-05 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0004_auto_20231107_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('time_seconds', models.IntegerField()),
                ('billable', models.BooleanField(default=False)),
                ('member', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('card', models.CharField(max_length=100)),
                ('card_labels', models.CharField(max_length=200)),
                ('estimate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estimate_seconds', models.IntegerField()),
                ('list', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('billable_time', models.DurationField()),
                ('billable_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('non_billable_time', models.DurationField()),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard_app.projeto')),
            ],
        ),
    ]
