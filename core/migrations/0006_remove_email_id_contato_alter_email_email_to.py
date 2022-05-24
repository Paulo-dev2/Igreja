# Generated by Django 4.0.4 on 2022-05-18 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_email_lidere_lider_email_lider_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='id_contato',
        ),
        migrations.AlterField(
            model_name='email',
            name='email_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contato'),
        ),
    ]
