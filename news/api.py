# Create your views here.
from django.db.models import Count
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import Check_API_KEY_Auth, ReadOnly
from comment.models import ActionType
from comment.serializers import CommentSerializer
from news.models import Submission, SubmissionType
from news.pagination import PaginationHandlerMixin
from news.serializers import SubmissionSerializer, SubmissionReadSerializer, SubmissionDetailedSerializer
from vote.models import Vote
from vote.serializers import VoteSerializerSubm


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class NewsApiView(APIView, PaginationHandlerMixin):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]
    pagination_class = BasicPagination
    permission_classes = [Check_API_KEY_Auth|ReadOnly]

    def get(self, request):
        news = Submission.objects.annotate(num_submissions=Count('votes')).order_by('-num_submissions')

        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(SubmissionReadSerializer(page, many=True).data)
        else:
            serializer = SubmissionReadSerializer(news, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data.get('title')
        url = request.data.get('url')
        text = request.data.get('text')
        user = request.user

        if url != "":
            url_exists = Submission.objects.filter(url=url)
            if url_exists.count() > 0:
                return Response(
                    {"res": "Url already exists", "id": url_exists[0].id},
                    status=status.HTTP_409_CONFLICT
                )
            submision_type = SubmissionType.objects.get(name="url")
            data = {
                'title': title,
                'type': submision_type.id,
                'author': user.id,
                'url': url,
                'points': 1,
            }
            serializer = SubmissionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                if text != "":
                    action_type = ActionType.objects.get(name="Submission")
                    data = {
                        "submission": serializer.data["id"],
                        "type": action_type.id,
                        "user": user.id,
                        "text": text
                    }
                    comment_serializer = CommentSerializer(data=data)
                    if comment_serializer.is_valid():
                        comment_serializer.save()
                        serializer.data["comments"].append(comment_serializer.data)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if text != "":
            submision_type = SubmissionType.objects.get(name="ask")
            data = {
                'title': title,
                'type': submision_type.id,
                'author': user.id,
                'text': text,
            }
            serializer = SubmissionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"res": "Los parametros pasados no son correctos"}, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailApiView(APIView):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]
    def get_object(self, submission_id):
        try:
            return Submission.objects.get(id=submission_id)
        except Submission.DoesNotExist:
            return None

    def get(self, request, news_id):
        submission_instance = self.get_object(news_id)
        if not submission_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SubmissionDetailedSerializer(submission_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, news_id):
        submission_instance = self.get_object(news_id)
        if not submission_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title')
        }
        if submission_instance.type == SubmissionType.objects.get(name="ask"):
            data["text"] = request.data.get('text')
        serializer = SubmissionSerializer(instance=submission_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, news_id):
        submission_instance = self.get_object(news_id)
        if not submission_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        submission_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_204_NO_CONTENT
        )


class NewsNewestApiView(APIView, PaginationHandlerMixin):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]
    pagination_class = BasicPagination

    def get(self, request):
        news = Submission.objects.order_by('-created_at')

        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(SubmissionReadSerializer(page, many=True).data)
        else:
            serializer = SubmissionReadSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsAskApiView(APIView, PaginationHandlerMixin):
    permission_classes = [Check_API_KEY_Auth | ReadOnly]
    pagination_class = BasicPagination

    def get(self, request):
        s_type = SubmissionType.objects.get(name="ask")
        news = Submission.objects.filter(type=s_type).annotate(num_submissions=Count('votes')).order_by('-num_submissions')

        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(SubmissionReadSerializer(page, many=True).data)
        else:
            serializer = SubmissionReadSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
