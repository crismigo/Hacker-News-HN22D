# Generated by Django 4.0.3 on 2022-04-14 13:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0002_user_about_user_karma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='karma',
        ),
    ]