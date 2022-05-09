
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment, ActionType
from comment.serializers import CommentSerializer
from vote.models import Vote
from vote.serializers import VoteSerializer


class CommentDetailApiView(APIView):
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


class CommentToCommentDetailApiView(APIView):
    def post(self, request, replied_comment_id):
        comment_type = ActionType.objects.get(name="Comment")
        data = {
            'type': comment_type,
            'user': request.user.id,
            'text': request.data.get('text'),
            'replied_comment': replied_comment_id
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentToSubmissionDetailApiView(APIView):
    def post(self, request, submission_id):
        submission_type = ActionType.objects.get(name="Submission")
        data = {
            'type': submission_type,
            'user': request.user.id,
            'text': request.data.get('text'),
            'submission': submission_id
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
        if (Vote.objects.filter(comment=self.get_comment(id)).exists()):
            return Response({"res: Vote already submitted."}, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = self.get_comment(id)
        if comment is None:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Vote.objects.filter(comment=comment).exists:
            return Response(
                {"res": "Vote doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            vote = Vote.objects.get(comment=comment).exists
            vote.delete()
            return Response(
                {"res": "Object deleted!"},
                status=status.HTTP_200_OK
            )
