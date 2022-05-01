from datetime import datetime

from django.conf import settings
from django.db import models

# Create your models here.
from news.models import Submission


class ActionType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Action Type"
        verbose_name_plural = "Action Types"

    def __str__(self):
        return self.name


class Comment(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, null=True, blank=True)
    replied_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(ActionType, on_delete=models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='self', related_name="comment_comments", through_fields=('replied_comment', 'user'),symmetrical=False)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='vote.Vote', related_name="comment_votes", through_fields=('comment', 'user'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.text

    def calculateseconds(self):
        datatime_now = datetime.now()

        dateyear = self.created_at.year
        datemonth = self.created_at.month
        dateday = self.created_at.day
        datehour = self.created_at.hour
        dateminute = self.created_at.minute
        datesecond = self.created_at.second
        then = datetime(dateyear, datemonth, dateday, datehour, dateminute, datesecond)
        duration = datatime_now - then
        return duration.total_seconds()

    def timesincecreation(self):
        duration_seconds = self.calculateseconds()
        days = divmod(duration_seconds, 86400)[0]
        hours = divmod(duration_seconds, 3600)[0]
        minutes = divmod(duration_seconds, 60)[0]

        if minutes > 59:
            if hours == 1:
                return str(int(hours)) + " hour ago"
            else:
                if hours > 23:
                    if days == 1:
                        return str(int(days)) + " day ago"
                    elif days < 365:
                        return str(int(days)) + " days ago"
                    else:
                        return self.created_at
                else:
                    return str(int(hours)) + " hours ago"
        else:
            if minutes == 1 or minutes == 0:
                return str(int(minutes)) + " minute ago"
            else:
                return str(int(minutes)) + " minutes ago"