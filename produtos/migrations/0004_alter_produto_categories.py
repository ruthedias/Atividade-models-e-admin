# Generated by Django 4.2.3 on 2024-12-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categories',
            field=models.ManyToManyField(related_name='categorias', to='produtos.categoria'),
        ),
    ]
