# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import Check_API_KEY_Auth, ReadOnly
from comment.models import Comment, ActionType
from comment.serializers import CommentSerializer
from news.models import Submission
from vote.models import Vote
from vote.serializers import VoteSerializerSubm


class CommentDetailApiView(APIView):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]

    def get_object(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return None

    def get(self, request, comment_id):
        comment_instance = self.get_object(comment_id)
        if not comment_instance:
            return Response(
                {"res": "Comment with comment id:{} does not exist".format(comment_id)},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CommentSerializer(comment_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentApiView(APIView):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]

    def post(self, request):
        if request.data.get('replied_comment'):
            comment_type = ActionType.objects.get(name="Comment")
            try:
                Comment.objects.get(id=request.data.get('replied_comment'))
            except Comment.DoesNotExist:
                return Response({"res": "replied_comment cannot be empty"},
                                status=status.HTTP_400_BAD_REQUEST)
            data = {
                'type': comment_type.id,
                'user': request.user.id,
                'text': request.data.get('text'),
                'replied_comment': request.data.get('replied_comment'),
                'submission': None,
            }
        else:
            submission_type = ActionType.objects.get(name="Submission")
            try:
                Submission.objects.get(id=request.data.get('submission'))
            except Submission.DoesNotExist:
                return Response({"res": "submission cannot be empty"},
                                status=status.HTTP_400_BAD_REQUEST)
            data = {
                'type': submission_type.id,
                'user': request.user.id,
                'text': request.data.get('text'),
                'submission': request.data.get('submission'),
                "replied_comment": None,
            }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            if data["replied_comment"] or data["submission"]:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"res":"submission or replied_comment cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
