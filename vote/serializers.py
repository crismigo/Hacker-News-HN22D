from rest_framework import serializers

from authentication.models import User
from comment.models import ActionType
from vote.models import Vote


class VoteSerializerSubm(serializers.ModelSerializer):


    class Meta:
        model = Vote
        fields = ["submission", "comment", "type", "user" , "created_at"]


class VoteSerializerComm(serializers.ModelSerializer):


    class Meta:
        model = Vote
        fields = ["submission", "comment", "type", "user", "created_at"]


