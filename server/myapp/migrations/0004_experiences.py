# Generated by Django 5.0.2 on 2024-03-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timePeriod', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
