import json
import random
import string

import requests
from django.contrib.auth import login, logout
from django.shortcuts import redirect

# Create your views here.
from .models import User

url_token = "https://api.fib.upc.edu/v2/o/token"
client_id = "Y0coFFuLKFGCecIR6qRA3PTn0OJuhQVFgNLQbW5Y"
client_secret = "i9qAbDlu1xN7AaLzuhfQMFYW0vrrIKY1iTHk3U0JPYmnKNA2aj71YJquZPBgD3PHCKzGANATbPcaZDjQXRHo0lGk7fJDBpFM21pVvBq1p7zLPlbNFQLcCTqPQ3nRbB9H"


def callBack(request):
    try:
        callback = request.build_absolute_uri('/auth/callback')
        authorization_code = request.GET.get("code")
        data = {"grant_type": "authorization_code",
                "redirect_uri": callback,
                "code": authorization_code,
                }
        result = requests.post(url_token, data=data, verify=True, allow_redirects=False,
                               auth=(client_id, client_secret))
        tokens = json.loads(result.text)
        access_token = tokens['access_token']
    except:
        return redirect("Home")

    try:
        api_call_headers = {'Authorization': 'Bearer ' + access_token, 'Accept': 'application/json'}
        api_call_response = requests.get("https://api.fib.upc.edu/v2/jo/", headers=api_call_headers, verify=True)
        user_data = json.loads(api_call_response.text)
        username = user_data["username"]
        back_page = request.session.get("back_page")
    except:
        return redirect("Home")
    try:
        user = User.objects.get(username=username)
        if not user.apiKey:
            user.apiKey = generate_key()
            user.save()
        login(request, user)
    except User.DoesNotExist:
        user = User(username=username)
        user.email = user_data["email"]
        user.first_name = user_data["nom"]
        user.last_name = user_data["cognoms"]
        user.apiKey = generate_key()
        user.save()
        login(request, user)

    return redirect(back_page)


def generate_key():
    chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"','').replace('\\', '')

    SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(32)])
    return SECRET_KEY

def loginView(request):
    callback = request.build_absolute_uri('/auth/callback')
    request.session["back_page"] = request.META.get('HTTP_REFERER')
    url_login = "https://api.fib.upc.edu/v2/o/authorize/?" + "client_id=" + client_id + "&redirect_uri=" + callback + "&response_type=code&state=random_state_string&approval_prompt=auto"
    return redirect(url_login)


def logoutView(request):
    try:
        logout(request)
        return redirect(request.META.get('HTTP_REFERER'))
    except:
        return redirect("Home")