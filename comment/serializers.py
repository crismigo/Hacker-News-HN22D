from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "submission", "replied_comment", "type", "user", "text", "comments", "votes", "created_at"]
