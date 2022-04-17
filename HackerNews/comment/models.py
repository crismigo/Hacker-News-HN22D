from django.db import models

# Create your models here.
from HackerNews import settings
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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        unique_together = [['submission', 'user'], ['replied_comment', 'user']]

    def __str__(self):
        return self.replied_comment
