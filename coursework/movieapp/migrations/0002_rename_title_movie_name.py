# Generated by Django 4.1.2 on 2022-10-24 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='name',
        ),
    ]
