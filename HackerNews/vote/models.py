from django.db import models

# Create your models here.
from comment.models import Comment, ActionType
from news.models import Submission
from HackerNews import settings


class Vote(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(ActionType, on_delete=models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"
        unique_together = [['submission', 'user'], ['comment', 'user']]

    def __str__(self):
        return self.submission, self.comment, self.type, self.user