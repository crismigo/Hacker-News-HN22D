# Generated by Django 4.0.3 on 2022-04-18 08:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_alter_user_options_remove_user_karma'),
        ('news', '0005_comment_comments_submission_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.ManyToManyField(related_name='comment_votes', through='news.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.ManyToManyField(related_name='comment_comments', through='news.Comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
