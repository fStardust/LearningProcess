# Generated by Django 5.1.4 on 2024-12-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='icon',
            field=models.CharField(max_length=100, verbose_name='币种图标'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=100, verbose_name='币种'),
        ),
    ]
