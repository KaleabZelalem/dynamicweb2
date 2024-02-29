# Generated by Django 5.0.2 on 2024-02-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_remove_movie_genre_movie_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_art',
            field=models.ImageField(upload_to=''),
        ),
    ]
