from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from comment.models import ActionType
from news.models import Submission
from news.serializers import SubmissionSerializer
from vote.models import Vote
from vote.serializers import VoteSerializer


class UserGetUpdateProfile(APIView):

    def get(self,request, user_id):
        dummy = ""

    def put(self,request, user_id):
        dummy = ""


class UserThreads(APIView):

    def get(self, request, user_id):
        dummy=""

class UserOwnSubmissions(APIView):

    def get(self, request, user_id):
        if User.objects.filter(id=user_id).exists():
            user = User.objects.get(id=user_id)
            submissions = Submission.objects.filter(author=user)
            serializer = SubmissionSerializer(submissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(
                {"res": "User with the id of the uri doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserUpvotedSubmissions(APIView):

    def get(self, request, user_id):
        act = ActionType.objects.get(name="Submission")
        if User.objects.filter(id=user_id).exists():
            user = User.objects.get(id=user_id)
            votes = Vote.objects.filter(user=user, type=act)

            serializer = VoteSerializer(votes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "User with the id of the uri doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserUpvotedComments(APIView):

    def get(self, request, user_id):
        act = ActionType.objects.get(name="Comment")
        if User.objects.filter(id=user_id).exists():
            user = User.objects.get(id=user_id)
            votes = Vote.objects.filter(user=user_id, type=act)

            serializer = VoteSerializer(votes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "User with the id of the uri doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )