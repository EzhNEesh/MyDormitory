# Generated by Django 3.2.16 on 2022-12-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_students_dormitory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
