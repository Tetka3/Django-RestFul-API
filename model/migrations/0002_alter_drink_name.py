# Generated by Django 4.2.7 on 2023-11-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
