# Generated by Django 4.0.4 on 2022-05-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_evento_preco_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta',
            name='data_start',
        ),
        migrations.AlterField(
            model_name='conta',
            name='data_end',
            field=models.DateTimeField(verbose_name='Data de vencimento'),
        ),
    ]