# Generated by Django 3.1 on 2024-06-18 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20240617_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='number',
            field=models.CharField(default=0, max_length=11),
        ),
    ]
