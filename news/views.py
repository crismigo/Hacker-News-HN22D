# Create your views here.
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import Submission, SubmissionType
from news.pagination import PaginationHandlerMixin
from news.serializers import SubmissionSerializer


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class NewsApiView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        news = Submission.objects.order_by('-points')

        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(SubmissionSerializer(page, many=True).data)
        else:
            serializer = SubmissionSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'type': request.data.get('type'),
            'author': request.data.get('author'),
            'url': request.data.get('url'),
            'text': request.data.get('text'),
        }
        serializer = SubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailApiView(APIView):

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

        serializer = SubmissionSerializer(submission_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, news_id):
        submission_instance = self.get_object(news_id)
        if not submission_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'type': request.data.get('type'),
            'author': request.data.get('author'),
            'url': request.data.get('url'),
            'text': request.data.get('text'),
        }
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
            status=status.HTTP_200_OK
        )


class NewsNewestApiView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        news = Submission.objects.order_by('-created_at')

        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(SubmissionSerializer(page, many=True).data)
        else:
            serializer = SubmissionSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsAskApiView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request):
        s_type = SubmissionType.objects.get(name="ask")
        news = Submission.objects.filter(type=s_type).order_by('-points')

        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(SubmissionSerializer(page, many=True).data)
        else:
            serializer = SubmissionSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
