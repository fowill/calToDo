# Generated by Django 3.0.4 on 2020-03-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='thing',
            old_name='content',
            new_name='status',
        ),
    ]