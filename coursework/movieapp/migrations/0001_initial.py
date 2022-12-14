# Generated by Django 4.1.2 on 2022-10-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date_released', models.DateField()),
                ('rating', models.IntegerField(default=0)),
                ('award_winning', models.BooleanField(default=False)),
            ],
        ),
    ]
