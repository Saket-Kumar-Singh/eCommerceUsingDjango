# Generated by Django 5.0.1 on 2024-01-24 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0006_alter_items_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car', to='Items.category'),
        ),
    ]
