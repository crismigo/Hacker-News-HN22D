from rest_framework import serializers

from authentication.models import User
from comment.models import Comment, ActionType
from vote.models import Vote
from vote.serializers import VoteSerializer


class CommentSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("getComments")
    votes = serializers.SerializerMethodField("getVotes")

    def getVotes(self, parent):
        comment_votes = Vote.objects.filter(comment_id=parent.id)
        votes = []
        for comm in comment_votes:
            serializer = VoteSerializer(comm)
            votes.append(serializer.data)
        return votes

    def getComments(self, parent):
        comment_comm = Comment.objects.filter(replied_comment_id=parent.id)
        comments = []
        for comm in comment_comm:
            serializer = CommentSerializer(comm)
            comments.append(serializer.data)
        return comments

    class Meta:
        model = Comment
        fields = ["id", "submission", "replied_comment", "type", "user", "text", "comments", "votes", "created_at"]


class CommentDetailedSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("getComments")
    votes = serializers.SerializerMethodField("getVotes")
    user = serializers.SerializerMethodField("getAuthor")
    type = serializers.SerializerMethodField("getType")

    def getVotes(self, parent):
        return Vote.objects.filter(comment_id=parent.id).count()+1

    def getComments(self, parent):
        comment_comm = Comment.objects.filter(replied_comment_id=parent.id)
        comments = []
        for comm in comment_comm:
            serializer = CommentDetailedSerializer(comm)
            comments.append(serializer.data)
        return comments

    def getAuthor(self, comment):
        user =User.objects.get(id=comment.user_id)
        return {"id":user.id, "username":user.username}

    def getType(self,comment):
        type =ActionType.objects.get(id=comment.type_id)
        return type.name

    class Meta:
        model = Comment
        fields = ["id", "submission", "replied_comment", "type", "user", "text", "comments", "votes", "created_at"]

class CommentThreadsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("getComments")
    votes = serializers.SerializerMethodField("getVotes")
    user = serializers.SerializerMethodField("getAuthor")
    type = serializers.SerializerMethodField("getType")

    def getVotes(self, parent):
        return Vote.objects.filter(comment_id=parent.id).count()+1

    def getComments(self, parent):
        comment_comm = Comment.objects.filter(replied_comment_id=parent.id)
        comments = []
        for comm in comment_comm:
            serializer = CommentDetailedSerializer(comm)
            comments.append(serializer.data)
        return comments

    def getAuthor(self, comment):
        user =User.objects.get(id=comment.user_id)
        return {"id":user.id, "username":user.username}

    def getType(self,comment):
        type =ActionType.objects.get(id=comment.type_id)
        return type.name

    class Meta:
        model = Comment
        fields = ["id", "submission", "replied_comment", "type", "user", "text", "comments", "votes", "created_at"]