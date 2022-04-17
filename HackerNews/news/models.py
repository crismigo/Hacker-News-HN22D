import datetime

from django.db import models
# Create your models here.
from django.conf import settings
from datetime import datetime

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
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.PositiveIntegerField(default=0)
    unvote = models.BooleanField(default=False)
    #hide = models.BooleanField(default=False) Al fer el filter no em funciona no se perque.
    hide = models.IntegerField(default=0)

    number_of_submissions= 30
    domainurlname = ""
    viewed_time = ""
    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

    def __str__(self):
        return self.title

    def markhide(self):
        self.hide= not self.hide

    def markunvote(self):
        self.unvote= not self.unvote

    def domainurl(self):
        from urllib.parse import urlparse
        if self.url is not None:
            self.domainurlname = urlparse(self.url).netloc
            self.domainurlname = "("+self.domainurlname+")"

    def timesincecreation(self):
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
                        self.viewed_time = str(int(days))+" days ago"
                    if days > 365:
                        self.viewed_time = self.created_at
                else:
                    self.viewed_time = str(int(hours)) + " hours ago"
        else:
            if minutes == 1 or minutes == 0:
                self.viewed_time = str(int(minutes)) + " minute ago"
            else:
                self.viewed_time = str(int(minutes)) + " minutes ago"

