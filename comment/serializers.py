from rest_framework import serializers
from comment.models import Comment
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
