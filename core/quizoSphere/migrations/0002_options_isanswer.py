# Generated by Django 5.0 on 2023-12-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizoSphere', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='isanswer',
            field=models.BooleanField(default=False),
        ),
    ]