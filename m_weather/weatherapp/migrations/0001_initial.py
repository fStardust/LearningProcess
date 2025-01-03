# Generated by Django 3.2.5 on 2022-03-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_time', models.DateTimeField()),
                ('choice_text', models.CharField(max_length=200)),
                ('correction', models.IntegerField(default=0)),
                ('self_index', models.IntegerField(default=100)),
                ('self_comment', models.TextField()),
            ],
            options={
                'verbose_name': 'Log Sheet',
                'verbose_name_plural': 'Log Sheet',
            },
        ),
        migrations.CreateModel(
            name='TrigTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trig_time_hour', models.CharField(default='8', max_length=8)),
                ('trig_time_min', models.CharField(default='30', max_length=8)),
                ('mod_date', models.DateTimeField(auto_now_add=True, verbose_name='修改日期')),
            ],
            options={
                'verbose_name': 'Triggering Time',
                'verbose_name_plural': 'Triggering Time',
            },
        ),
    ]
