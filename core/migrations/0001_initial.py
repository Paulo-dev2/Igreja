# Generated by Django 4.0.4 on 2022-05-12 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('data_start', models.DateTimeField(auto_now_add=True)),
                ('data_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('setor', models.CharField(max_length=50)),
                ('descrition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('value', models.FloatField()),
                ('descrition', models.TextField()),
                ('data_start', models.DateTimeField(auto_now_add=True)),
                ('data_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_from', models.CharField(max_length=120)),
                ('email_from', models.CharField(max_length=120)),
                ('text_from', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dizimo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=15)),
                ('tel', models.CharField(max_length=15)),
                ('value', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, help_text='Size: 1920x570', upload_to='')),
                ('quantidade_ingressos', models.IntegerField(blank=True)),
                ('preco', models.FloatField(blank=True)),
                ('vinculo', models.CharField(blank=True, max_length=70)),
                ('data_start', models.DateTimeField()),
                ('data_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Igreja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cnpj', models.CharField(max_length=16)),
                ('uf', models.CharField(max_length=25)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=25)),
                ('cidade', models.CharField(max_length=70)),
                ('rua', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=15)),
                ('tel', models.CharField(max_length=15)),
                ('value', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('subTitle', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, help_text='Size: 1920x570', upload_to='slides/')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption1', models.CharField(max_length=100)),
                ('caption2', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, help_text='Size: 1920x570', upload_to='slides/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Systema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=11)),
                ('tipo', models.IntegerField()),
                ('image', models.FileField(blank=True, null=True, upload_to='sys/')),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=150)),
                ('id_cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Lideres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lidere', models.CharField(max_length=120)),
                ('email_lidere', models.CharField(max_length=120)),
                ('numero_lideres', models.CharField(max_length=120)),
                ('setor_lider', models.CharField(max_length=120)),
                ('id_cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('email_to', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('id_contato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contato')),
            ],
        ),
    ]
