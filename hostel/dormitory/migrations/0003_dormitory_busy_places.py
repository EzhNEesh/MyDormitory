# Generated by Django 3.2.16 on 2022-12-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0002_alter_dormitory_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitory',
            name='busy_places',
            field=models.IntegerField(default=357),
        ),
    ]
