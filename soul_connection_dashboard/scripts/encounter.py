import os
import django
import requests
from rest_framework import status
from rest_framework.response import Response
from encounters.models import Encounter
from customer.models import Customer
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
    url_encounter = "https://soul-connection.fr/api/encounters"
    headers = {
        'accept': 'application/json',
        'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
        'Authorization' : f'Bearer {token}',
        #'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiJqZWFubmUubWFydGluQHNvdWwtY29ubmVjdGlvbi5mciIsIm5hbWUiOiJKZWFubmUiLCJzdXJuYW1lIjoiTWFydGluIiwiZXhwIjoxNzI3MzM4NDMyfQ.H1NsLsQjJiMPA97oYkslaPOwUA0PhE1LynUJQQOX0vQ',
    }
    response_token = requests.get(url_encounter, headers=headers)
    transform_request = response_token.json()
    check = Encounter.objects.all()
    for i in transform_request:
        encounter = Encounter()
        url_encounter_id = f"https://soul-connection.fr/api/encounters/{i.get('id')}"
        response_id = requests.get(url_encounter_id, headers=headers)
        
        try :
            get_response = response_id.json()
        except ValueError:
            print(f"Get_response: Error of JSON decodge: {url_encounter_id}")
            continue

        customer  = Customer.objects.get(id=i.get('customer_id'))
        encounter.id = get_response.get("id")
        encounter.customer = customer
        encounter.date = get_response.get("date")
        encounter.rating = get_response.get("rating")
        encounter.comment = get_response.get("comment")
        encounter.source = get_response.get("source")
        if encounter in check:
            continue
        encounter.save()
