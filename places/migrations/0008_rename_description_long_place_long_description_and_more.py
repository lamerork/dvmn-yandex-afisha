# Generated by Django 4.2.6 on 2023-11-04 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_place_alter_place_description_short_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
