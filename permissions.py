from django.conf import settings

from rest_framework.permissions import BasePermission


class Check_API_KEY_Auth(BasePermission):

    def has_permission(self, request, view):
        key = request.META.get('API_KEY')
        return key == settings.API_KEY
