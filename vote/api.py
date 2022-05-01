from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from news.models import Submission
from vote.models import Vote
from vote.serializers import VoteSerializer

class VotesDetailApiView(APIView):

    def get_submission(self, submission_id):
        try:
            return Submission.objects.get(id=submission_id)
        except Submission.DoesNotExist:
            return None

    def get_comment(self,comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return None

    def post(self, request):
        data = {
            'submission': request.data.get('submission'),
            'comment': request.data.get('comment'),
            'type': request.data.get('type'),
            'user': request.data.get('user'),
        }
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        aux = False
        submission = self.get_submission(id)
        comment = None
        if submission is None:
            aux = True
            comment = self.get_comment(id)
            if comment is None:
                return Response(
                    {"res": "Object with todo id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        if not aux:
            vote = Vote.objects.get(submission=submission)
        else :
            vote = Vote.objects.get(comment=comment)
        vote.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )






