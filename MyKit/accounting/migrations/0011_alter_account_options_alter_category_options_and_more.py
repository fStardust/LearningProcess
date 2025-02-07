# Generated by Django 5.1.4 on 2024-12-25 22:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_alter_currency_icon_alter_currency_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['created_date'], 'verbose_name': '账户', 'verbose_name_plural': '账户'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['id'], 'verbose_name': '货币', 'verbose_name_plural': '货币'},
        ),
        migrations.AlterModelOptions(
            name='historyrecord',
            options={'ordering': ['-time_of_occurrence'], 'verbose_name': '交易记录', 'verbose_name_plural': '交易记录'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id'], 'verbose_name': '子类别', 'verbose_name_plural': '子类别'},
        ),
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.currency', verbose_name='货币'),
        ),
        migrations.AlterField(
            model_name='account',
            name='icon',
            field=models.CharField(max_length=100, null=True, verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=100, verbose_name='账户名称'),
        ),
        migrations.AlterField(
            model_name='account',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('expense', '支出'), ('income', '收入')], default='支出', max_length=100, verbose_name='类别类型'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=100, verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='类别名称'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='account',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.account', verbose_name='账户'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='currency',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.currency', verbose_name='货币'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.subcategory', verbose_name='子类别'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='time_of_occurrence',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发生时间'),
        ),
        migrations.AlterField(
            model_name='historyrecord',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日期'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='icon',
            field=models.CharField(max_length=100, verbose_name='图标'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='子类别名称'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.category', verbose_name='父类别'),
        ),
    ]
