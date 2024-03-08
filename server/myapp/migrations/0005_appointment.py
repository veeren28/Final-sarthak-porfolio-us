# Generated by Django 5.0.2 on 2024-03-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_experiences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
            ],
        ),
    ]