# Generated by Django 5.1.1 on 2024-10-18 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Auto',
        ),
    ]