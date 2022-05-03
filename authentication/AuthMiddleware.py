from django.http import HttpResponse

def Auth_API_Key(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        key = 'Api-Key'

        if not hasattr(request, 'user') or not request.user.is_authenticated:
            response = get_response(request)

        elif request.user.is_authenticated and request.user.apiKey == request.headers.get('Authorization'):
            response = get_response(request)

        else:
            response = HttpResponse('401 : Unauthorized', status=401)

        #response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

