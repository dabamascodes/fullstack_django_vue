# Generated by Django 5.1.6 on 2025-02-13 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='description',
            new_name='descripcion',
        ),
    ]
