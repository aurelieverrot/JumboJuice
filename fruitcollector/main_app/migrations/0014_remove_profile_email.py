# Generated by Django 3.0.4 on 2020-03-24 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_merge_20200324_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
