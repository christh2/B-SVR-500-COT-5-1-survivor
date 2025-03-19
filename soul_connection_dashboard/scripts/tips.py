import os
import django
import requests
from rest_framework import status
from rest_framework.response import Response
from tips.models import Tip
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soul_connection_dashboard.settings')
django.setup()


def login_view():
    url_soul = "https://soul-connection.fr/api/employees/login"
    request = {
            'email': 'jeanne.martin@soul-connection.fr',
            'password': 'naouLeA82oeirn',
    }
    headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
    }
    response_token = requests.post(url_soul, json={'email': request['email'], 'password': request['password']},headers=headers)

    if response_token.status_code == 200:
        response_to_it = response_token.json()
        stock_response = response_to_it["access_token"]
        return stock_response
        #return Response({'access_token': stock_response}, status=status.HTTP_200_OK)
    if response_token.status_code == 401:
        return Response({'invalid_credentials': 'Invalid Email and Password combination.'})
    if response_token.status_code == 422:
        return Response({'Bad_token': 'Token not found'})

def run():
    token = login_view()
    if token is None:
        print("Invalid token")
        return
    url_tips = "https://soul-connection.fr/api/tips"
    headers = {
        'accept': 'application/json',
        'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
        'Authorization' : f'Bearer {token}',
        #'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiJqZWFubmUubWFydGluQHNvdWwtY29ubmVjdGlvbi5mciIsIm5hbWUiOiJKZWFubmUiLCJzdXJuYW1lIjoiTWFydGluIiwiZXhwIjoxNzI3MzM4NDMyfQ.H1NsLsQjJiMPA97oYkslaPOwUA0PhE1LynUJQQOX0vQ',
    }

    response_token = requests.get(url_tips, headers=headers)
    try :
        transform_request = response_token.json()
    except ValueError:
        print(f"Get_response: Error of JSON decodge: {url_tips}")
    check = Tip.objects.all()
    for i in transform_request:
        tip = Tip()
        
        tip.id = i.get("id")
        tip.title = i.get("title")
        tip.tip = i.get("tip")
        if tip in check:
            continue
        tip.save()
