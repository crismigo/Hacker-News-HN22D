from rest_framework import serializers

from comment.models import Comment
from comment.serializers import CommentSerializer
from news.models import Submission
from vote.models import Vote
from vote.serializers import VoteSerializer


def getRepliedComments(comment):
    replied_comments = Comment.objects.filter(replied_comment=comment.id)
    comments = []
    for comment in replied_comments:
        comment["replied_comments"] = getRepliedComments(comment)
        comments.append(comment)

    return comments


class SubmissionSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("getComments")
    votes = serializers.SerializerMethodField("getVotes")

    def getVotes(self,submission):
        subm_votes = Vote.objects.filter(submission_id=submission.id)
        votes = []
        for comm in subm_votes:
            serializer = VoteSerializer(comm)
            votes.append(serializer.data)
        return votes

    def getComments(self,submission):
        subm_comm=Comment.objects.filter(submission_id=submission.id)
        comments=[]
        for comm in subm_comm:
            serializer = CommentSerializer(comm)
            comments.append(serializer.data)
        return comments



    class Meta:
        model = Submission
        fields = ["id", "title", "type", "author", "url", "text", "points", "comments", "votes", "created_at"]
