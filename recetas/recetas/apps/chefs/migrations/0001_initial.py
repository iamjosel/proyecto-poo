# Generated by Django 3.2.25 on 2024-10-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('PAS', 'Pasaporte')], max_length=5)),
                ('nombres', models.CharField(max_length=70)),
                ('apellidos', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]