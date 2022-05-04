from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment, ActionType
from news.models import Submission
from news.serializers import SubmissionSerializer
from vote.models import Vote
from vote.serializers import VoteSerializer

class VoteSubmissionApiView(APIView):

    def get_submission(self, submission_id):
        try:
            return Submission.objects.get(id=submission_id)
        except Submission.DoesNotExist:
            return None

    def get(self, request,id):
        votes = Vote.objects.all()
        if not votes:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VoteSerializer(votes,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        act = ActionType.objects.get(name="Submission")

        data = {
            'submission': id,
            'comment': None,
            'type': act.id,
            'user': request.user.id,
        }
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        submission = self.get_submission(id)
        if submission is None:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        vote = Vote.objects.get(submission=submission)
        if vote is None:
            return Response(
                {"res": "Vote doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        vote.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class VoteCommentApiView(APIView):
    def get_comment(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return None

    def post(self, request, id):
        act = ActionType.objects.get(name="Comment")
        data = {
            'submission': None,
            'comment': id,
            'type': act.id,
            'user': request.user.id,
        }
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = self.get_comment(id)
        if comment is None:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        vote = Vote.objects.get(comment=comment)
        if vote is None:
            return Response(
                {"res": "Vote doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        vote.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )














