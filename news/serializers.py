from rest_framework import serializers

from authentication.models import User
from comment.models import Comment
from comment.serializers import CommentSerializer, CommentDetailedSerializer
from news.models import Submission, SubmissionType
from vote.models import Vote
from vote.serializers import VoteSerializerSubm

def getRepliedComments(comment):
    replied_comments = Comment.objects.filter(replied_comment=comment.id)
    comments = 0
    for comm in replied_comments:
        comments += getRepliedComments(comm)
        comments += 1

    return comments


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id", "title", "type", "author", "url", "text", "points", "comments", "votes", "created_at"]


class SubmissionReadSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("getComments")
    votes = serializers.SerializerMethodField("getVotes")
    author = serializers.SerializerMethodField("getAuthor")
    type = serializers.SerializerMethodField("getType")

    def getVotes(self, submission):
        return Vote.objects.filter(submission_id=submission.id).count() +1

    def getComments(self, submission):
        subm_comm = Comment.objects.filter(submission_id=submission.id)
        comments = 0
        for comm in subm_comm:
            comments += getRepliedComments(comm)
            comments += 1

        return comments

    def getAuthor(self, submission):
        user =User.objects.get(id=submission.author_id)
        return {"id":user.id, "username":user.username}

    def getType(self,submission):
        type =SubmissionType.objects.get(id=submission.type_id)
        return type.name

    class Meta:
        model = Submission
        fields = ["id", "title", "type", "author", "url", "text", "comments", "votes", "created_at"]


class SubmissionDetailedSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("getComments")
    votes = serializers.SerializerMethodField("getVotes")

    def getVotes(self, submission):
        return Vote.objects.filter(submission_id=submission.id).count() + 1

    def getComments(self, submission):
        subm_comm = Comment.objects.filter(submission_id=submission.id)
        comments = []
        for comm in subm_comm:
            serializer = CommentDetailedSerializer(comm)
            comments.append(serializer.data)
        return comments

    def getAuthor(self, submission):
        user =User.objects.get(id=submission.author_id)
        return {"id":user.id, "username":user.username}

    def getType(self,submission):
        type =SubmissionType.objects.get(id=submission.type_id)
        return type.name

    author = serializers.SerializerMethodField("getAuthor")
    type = serializers.SerializerMethodField("getType")

    class Meta:
        model = Submission
        fields = ["id", "title", "type", "author", "url", "text", "comments", "votes", "created_at"]
