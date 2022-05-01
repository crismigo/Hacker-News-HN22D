from rest_framework import serializers

from comment.models import Comment
from vote.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["submission", "comment", "type", "user" , "created_at"]


