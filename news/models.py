from datetime import datetime

from django.conf import settings
from django.db import models
# Create your models here.
class SubmissionType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Submission Type"
        verbose_name_plural = "Submission Types"

    def __str__(self):
        return self.name


class Submission(models.Model):
    title = models.CharField(max_length=100, blank=False)
    type = models.ForeignKey(SubmissionType, on_delete=models.RESTRICT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    points = models.PositiveIntegerField(default=1)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='comment.Comment', related_name="comments", through_fields=('submission', 'user'))
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='vote.Vote', related_name="votes", through_fields=('submission', 'user'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

    def __str__(self):
        return self.title

    def domainurl(self):
        from urllib.parse import urlparse
        submtype = SubmissionType.objects.get(name="ask")
        if self.url is not None and submtype != self.type:
            return "(" + urlparse(self.url).netloc + ")"
        else:
            return ""

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
