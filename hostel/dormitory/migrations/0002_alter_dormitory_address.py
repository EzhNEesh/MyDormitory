# Generated by Django 3.2.16 on 2022-12-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormitory',
            name='address',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
