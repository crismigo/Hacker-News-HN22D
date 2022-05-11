
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import Check_API_KEY_Auth, ReadOnly
from comment.models import Comment, ActionType
from comment.serializers import CommentSerializer
from vote.models import Vote
from vote.serializers import VoteSerializer


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
            data = {
                'type': comment_type.id,
                'user': request.user.id,
                'text': request.data.get('text'),
                'replied_comment': request.data.get('replied_comment'),
                'submission': "",
            }
        else:
            submission_type = ActionType.objects.get(name="Submission")
            data = {
                'type': submission_type.id,
                'user': request.user.id,
                'text': request.data.get('text'),
                'submission': request.data.get('submission'),
                "replied_comment":"",
            }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




