# Generated by Django 4.0.4 on 2022-04-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='Publishing',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]