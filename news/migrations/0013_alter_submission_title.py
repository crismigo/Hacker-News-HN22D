# Generated by Django 4.0.3 on 2022-04-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_submission_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
