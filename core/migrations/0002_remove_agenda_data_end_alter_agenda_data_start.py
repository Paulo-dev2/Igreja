# Generated by Django 4.0.4 on 2022-05-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='data_end',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data_start',
            field=models.DateTimeField(verbose_name='Dia marcado'),
        ),
    ]
