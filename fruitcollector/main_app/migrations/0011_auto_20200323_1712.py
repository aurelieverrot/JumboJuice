# Generated by Django 3.0.4 on 2020-03-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20200322_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitamin',
            name='name',
            field=models.CharField(choices=[('A', 'Necessary for proper vision and organ function.'), ('B1', 'Helps convert nutrients into energy.'), ('B2', 'Necessary for energy production, cell function and fat metabolism.'), ('B3', 'Drives the production of energy from food.'), ('B5', 'Necessary for fatty acid synthesis.'), ('B6', 'Helps your body release sugar from stored carbohydrates for energy and create red blood cells.'), ('B7', 'Plays a role in the metabolism of fatty acids, amino acids and glucose.'), ('B9', 'Important for proper cell division.'), ('B12', 'Necessary for red blood cell formation and proper nervous system and brain function.'), ('C', 'Required for the creation of neurotransmitters and collagen, the main protein in your skin.'), ('D', 'Promotes proper immune function and assists in calcium absorption and bone growth.'), ('E', 'Assists immune function and acts as an antioxidant that protects cells from damage.'), ('K', 'Required for blood clotting and proper bone development.')], default='A', max_length=5),
        ),
    ]
