# Generated by Django 3.0.7 on 2020-06-19 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0005_auto_20200619_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
