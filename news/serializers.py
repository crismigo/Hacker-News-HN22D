from rest_framework import serializers

from comment.models import Comment
from news.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id", "title", "type", "author", "url", "text", "points", "comments", "votes", "created_at"]
