from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    about = models.TextField(null=True, blank=True)
    viewed_time = ""

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def timeSinceCreation(self):
        datatime_now = datetime.now()

        dateyear = self.date_joined.year
        datemonth = self.date_joined.month
        dateday = self.date_joined.day
        datehour = self.date_joined.hour
        dateminute = self.date_joined.minute
        datesecond = self.date_joined.second
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
                        self.viewed_time = self.date_joined
                else:
                    self.viewed_time = str(int(hours)) + " hours ago"
        else:
            if minutes == 1 or minutes == 0:
                self.viewed_time = str(int(minutes)) + " minute ago"
            else:
                self.viewed_time = str(int(minutes)) + " minutes ago"
