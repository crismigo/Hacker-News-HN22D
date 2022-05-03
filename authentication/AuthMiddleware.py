from django.http import HttpResponse


class Auth_API_Key:

    def simple_middleware(get_response):
        # One-time configuration and initialization.

        def middleware(request):
            # Code to be executed for each request before
            # the view (and later middleware) are called.
            key = request.META['HTTP_AUTHORIZATION']
            if request.user.apiKey == key:
                response = get_response(request)
            else :
                response = HttpResponse('Unauthorized', status=401)
            # Code to be executed for each request/response after
            # the view is called.

            return response

        return middleware