from rest_framework import serializers

from authentication.models import User
from comment.models import Comment
from vote.models import Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "date_joined", "about"]