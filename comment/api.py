from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializers import CommentSerializer


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

    def post(self, request):
        data = {
            'type': request.data.get('type'),
            'user': request.data.get('user'),
            'text': request.data.get('text'),
        }