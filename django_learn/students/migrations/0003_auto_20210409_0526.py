# Generated by Django 2.1.7 on 2021-04-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210408_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', through='students.Enroll', to='students.Student'),
        ),
    ]
