# Generated by Django 4.1.7 on 2023-06-11 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_rename_imagie_games_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='special_games',
            old_name='imagie',
            new_name='image',
        ),
    ]
