# Generated by Django 4.0.3 on 2022-05-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='apiKey',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
