# Generated by Django 4.2.6 on 2023-10-09 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
    ]