# Generated by Django 4.0.3 on 2022-03-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='consultation_date',
            field=models.DateTimeField(null=True),
        ),
    ]