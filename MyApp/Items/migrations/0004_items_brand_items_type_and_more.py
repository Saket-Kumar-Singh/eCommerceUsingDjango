# Generated by Django 5.0.1 on 2024-01-24 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_country_alter_items_options_items_image_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='brand',
            field=models.ForeignKey(default='Local', on_delete=django.db.models.deletion.CASCADE, related_name='car', to='Items.company'),
        ),
        migrations.AddField(
            model_name='items',
            name='type',
            field=models.ForeignKey(default='4 pahiya', on_delete=django.db.models.deletion.CASCADE, related_name='Car', to='Items.category'),
        ),
        migrations.AlterField(
            model_name='company',
            name='Country_of_origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Companies', to='Items.country'),
        ),
    ]