# Generated by Django 4.2.7 on 2024-01-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-02-19'),
            preserve_default=False,
        ),
    ]
