# Generated by Django 4.2.1 on 2023-06-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_games_imagie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagie', models.ImageField(upload_to='gamecovers/')),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='games',
            name='deleted_at',
        ),
        migrations.AlterField(
            model_name='games',
            name='imagie',
            field=models.ImageField(upload_to='gamecovers/'),
        ),
    ]
