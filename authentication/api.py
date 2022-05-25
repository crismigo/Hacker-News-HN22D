import json
import random
import string

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User

url_token = "https://api.fib.upc.edu/v2/o/token"
client_id = "Y0coFFuLKFGCecIR6qRA3PTn0OJuhQVFgNLQbW5Y"
client_secret = "i9qAbDlu1xN7AaLzuhfQMFYW0vrrIKY1iTHk3U0JPYmnKNA2aj71YJquZPBgD3PHCKzGANATbPcaZDjQXRHo0lGk7fJDBpFM21pVvBq1p7zLPlbNFQLcCTqPQ3nRbB9H"

class LoginCallback(APIView):
    def post(self,request):
        access_token = request.GET.get("access_token")

        try:
            api_call_headers = {'Authorization': 'Bearer ' + access_token, 'Accept': 'application/json'}
            api_call_response = requests.get("https://api.fib.upc.edu/v2/jo/", headers=api_call_headers, verify=True)
            user_data = json.loads(api_call_response.text)
            username = user_data["username"]
        except:
            return Response(
                {"res": "No s'ha pogut obtenir la informacio de l'usuari"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(username=username)
            if not user.apiKey:
                user.apiKey = generate_key()
                user.save()
            data = {
                "id" : user.id,
                "username": user.username,
                "apiKey": user.apiKey
            }
            return Response(data, status=status.HTTP_200_OK )

        except User.DoesNotExist:
            user = User(username=username)
            user.email = user_data["email"]
            user.first_name = user_data["nom"]
            user.last_name = user_data["cognoms"]
            user.apiKey = generate_key()
            user.save()
            data = {
                "id": user.id,
                "username": user.username,
                "apiKey": user.apiKey
            }
            return Response(data, status=status.HTTP_200_OK)

def generate_key():
    chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"','').replace('\\', '')

    SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(32)])
    return SECRET_KEY