from django.http import HttpResponse
from .models import User


def Auth_API_Key(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        key = 'Api-Key'

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            tmp_user = User.objects.get(username=request.user.username)
            if request.user.is_authenticated and request.user.apiKey == tmp_user.apiKey:
                response = get_response(request)
            else:
                response = HttpResponse('401 : Unauthorized', status=401)

        else:
            response = HttpResponse('401 : Unauthorized', status=401)

        # response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
