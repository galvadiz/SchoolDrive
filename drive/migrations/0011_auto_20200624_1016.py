# Generated by Django 3.0.7 on 2020-06-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0010_auto_20200622_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='fecha_upload',
            field=models.DateField(default='2020-06-24'),
        ),
        migrations.AlterField(
            model_name='carpeta',
            name='fecha_creacion',
            field=models.DateField(default='2020-06-24'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default='2020-06-24'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2020-06-24'),
        ),
    ]
