# Generated by Django 4.2 on 2024-08-05 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('release_year', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='album-images')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album_manager.autor')),
            ],
        ),
    ]
