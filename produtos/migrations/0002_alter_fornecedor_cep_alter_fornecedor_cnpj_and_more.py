# Generated by Django 4.2.3 on 2024-12-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='rua',
            field=models.CharField(max_length=150),
        ),
    ]