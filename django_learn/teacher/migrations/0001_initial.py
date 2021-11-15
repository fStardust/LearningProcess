# Generated by Django 2.1.7 on 2021-04-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.SmallIntegerField()),
                ('height', models.IntegerField(null=True)),
                ('sex', models.SmallIntegerField(default=1)),
                ('qq', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('x_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
    ]
