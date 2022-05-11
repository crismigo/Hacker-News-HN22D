from rest_framework import serializers

from authentication.models import User
from comment.models import ActionType
from vote.models import Vote


class VoteSerializerSubm(serializers.ModelSerializer):
    type = serializers.SerializerMethodField("getType")

    def getType(self,submission):
        type = ActionType.objects.get(name="Submission")
        return type.name

    class Meta:
        model = Vote
        fields = ["submission", "comment", "type", "user" , "created_at"]


class VoteSerializerComm(serializers.ModelSerializer):
    type = serializers.SerializerMethodField("getType")
    def getType(self,submission):
        type = ActionType.objects.get(name="Comment")
        return type.name

    class Meta:
        model = Vote
        fields = ["submission", "comment", "type", "user", "created_at"]


