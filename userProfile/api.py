from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.permissions import Check_API_KEY_Auth, ReadOnly
from comment.serializers import CommentThreadsSerializer
from comment.models import ActionType, Comment
from comment.serializers import CommentSerializer
from news.models import Submission
from news.serializers import SubmissionReadSerializer
from userProfile.serializers import UserSerializer
from vote.models import Vote

class UserGetUpdateProfile(APIView):

    permission_classes = [Check_API_KEY_Auth | ReadOnly]

    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "User with the id doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "User with the id doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'email': request.data.get('email'),
            'about': request.data.get('about'),
        }
        serializer = UserSerializer(instance=user_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserThreads(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "User with the id doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        comments = Comment.objects.filter(user_id=user_instance.id)
        serializer = CommentThreadsSerializer(comments,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserOwnSubmissions(APIView):

    def get(self, request, user_id):
        if User.objects.filter(id=user_id).exists():
            user = User.objects.get(id=user_id)
            submissions = Submission.objects.filter(author=user)
            serializer = SubmissionReadSerializer(submissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "User with the id of the uri doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserUpvotedSubmissions(APIView):
    permission_classes = [Check_API_KEY_Auth]
    def get(self, request):
        act = ActionType.objects.get(name="Submission")
        if User.objects.filter(id=request.user.id).exists():
            user = User.objects.get(id=request.user.id)
            votes = Vote.objects.filter(user=user, type=act)
            submissions = []
            for vote in votes:
                submissions.append(Submission.objects.get(id=vote.submission.id))
            serializer = SubmissionReadSerializer(submissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "User with the id of the uri doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserUpvotedComments(APIView):
    permission_classes = [Check_API_KEY_Auth]
    def get(self, request):
        act = ActionType.objects.get(name="Comment")
        if User.objects.filter(id=request.user.id).exists():
            user = User.objects.get(id=request.user.id)
            votes = Vote.objects.filter(user=user, type=act)
            comments = []
            for vote in votes:
                comments.append(Comment.objects.get(id=vote.comment.id))
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "User with the id of the uri doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
