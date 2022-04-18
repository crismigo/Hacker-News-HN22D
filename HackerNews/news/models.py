import datetime

from django.db import models
# Create your models here.
from django.conf import settings
from datetime import datetime
from django import template

unvoting = template.Library()

class SubmissionType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Submission Type"
        verbose_name_plural = "Submission Types"

    def __str__(self):
        return self.name


class Submission(models.Model):
    title = models.CharField(max_length=50, blank=False)
    type = models.ForeignKey(SubmissionType, on_delete=models.RESTRICT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    points = models.PositiveIntegerField(default=1)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name="comments",
                                      through_fields=('submission', 'user'))
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Vote', related_name="votes",
                                   through_fields=('submission', 'user'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

    def __str__(self):
        return self.title


    def domainurl(self):
        from urllib.parse import urlparse
        if self.url is not None:
            return  "(" +  urlparse(self.url).netloc + ")"

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
    """ TODO: A l'hora de mirar si el usuari ja ha votat o no, django no dona la possibilitat de passar parametres del html,
    en el nostre cas el usuari que fa la request.
    @unvoting.filter
     """

    def timesincecreation(self):
        duration_seconds= self.calculateseconds()
        days = divmod(duration_seconds, 86400)[0]
        hours = divmod(duration_seconds, 3600)[0]
        minutes = divmod(duration_seconds, 60)[0]


        if minutes > 59:
            if hours == 1:
                return str(int(days)) + " hour ago"
            else:
                if hours > 23:
                    if days == 1:
                        return str(int(days)) + " day ago"
                    elif days < 365:
                        return str(int(days))+" days ago"
                    else :
                        return self.created_at
                else:
                    return str(int(hours)) + " hours ago"
        else:
            if minutes == 1 or minutes == 0:
                return str(int(minutes)) + " minute ago"
            else:
                return str(int(minutes)) + " minutes ago"


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
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name="comment_comments",
                                      through_fields=('replied_comment', 'user'))
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Vote', related_name="comment_votes",
                                   through_fields=('comment', 'user'))
    created_at = models.DateTimeField(auto_now_add=True)
    viewed_time = ""

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        unique_together = [['submission', 'user'], ['replied_comment', 'user']]

    def __str__(self):
        return self.text

    def timeSinceCreation(self):
        datatime_now = datetime.now()

        dateyear = self.created_at.year
        datemonth = self.created_at.month
        dateday = self.created_at.day
        datehour = self.created_at.hour
        dateminute = self.created_at.minute
        datesecond = self.created_at.second
        then = datetime(dateyear, datemonth, dateday, datehour, dateminute, datesecond)

        duration = datatime_now - then
        duration_seconds = duration.total_seconds()
        days = divmod(duration_seconds, 86400)[0]
        hours = divmod(duration_seconds, 3600)[0]
        minutes = divmod(duration_seconds, 60)[0]

        if minutes > 59:
            if hours == 1:
                self.viewed_time = str(int(days)) + " hour ago"
            else:
                if hours > 23:
                    if days == 1:
                        self.viewed_time = str(int(days)) + " day ago"
                    else:
                        self.viewed_time = str(int(days)) + " days ago"
                    if days > 365:
                        self.viewed_time = self.created_at
                else:
                    self.viewed_time = str(int(hours)) + " hours ago"
        else:
            if minutes == 1 or minutes == 0:
                self.viewed_time = str(int(minutes)) + " minute ago"
            else:
                self.viewed_time = str(int(minutes)) + " minutes ago"


class Vote(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(ActionType, on_delete=models.RESTRICT,default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"
        unique_together = [['submission', 'user'], ['comment', 'user']]

    def __str__(self):
        return self.user_id
