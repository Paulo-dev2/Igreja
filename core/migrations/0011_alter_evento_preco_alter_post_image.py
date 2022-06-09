# Generated by Django 4.0.4 on 2022-05-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_post_subtitle_post_author_post_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='preco',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Tamanho maximo 4MB', upload_to='posts/'),
        ),
    ]