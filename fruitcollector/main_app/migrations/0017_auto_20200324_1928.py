# Generated by Django 3.0.4 on 2020-03-24 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20200324_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fav_juice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Juice'),
        ),
    ]
