from django.conf import settings

from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import login, logout

from authentication.models import User


class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        key = request.headers.get('Authorization')
        if key:
            user = User.objects.filter(apiKey=key)
            if user.count()>0:
                login(request,user[0])
                return True
        logout(request)
        return False

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
