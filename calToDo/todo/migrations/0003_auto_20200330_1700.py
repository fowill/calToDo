# Generated by Django 3.0.4 on 2020-03-30 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200325_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
