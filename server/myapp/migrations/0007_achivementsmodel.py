# Generated by Django 5.0.2 on 2024-03-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_appointment_appointmentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchivementsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=5)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]