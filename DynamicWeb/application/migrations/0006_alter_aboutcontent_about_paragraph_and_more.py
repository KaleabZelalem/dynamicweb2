# Generated by Django 5.0.2 on 2024-02-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_aboutcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontent',
            name='about_paragraph',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutcontent',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aboutcontent',
            name='mission',
            field=models.CharField(max_length=500),
        ),
    ]
