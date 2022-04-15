from django.db import models

# Create your models here.
from django.conf import settings


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
    url =  models.TextField(blank=True)
    text = models.TextField(blank=True)
    points = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

    def __str__(self):
        return self.title
