# Generated by Django 4.0.3 on 2022-04-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]