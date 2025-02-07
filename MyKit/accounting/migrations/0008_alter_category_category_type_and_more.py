# Generated by Django 5.1.4 on 2024-12-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_alter_category_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('income', '收入'), ('expense', '支出')], default='income', max_length=100),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
