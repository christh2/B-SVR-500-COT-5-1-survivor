import os
import django
import requests
from rest_framework import status
from rest_framework.response import Response
from events.models import Event
from coach.models import Employee
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
    url_event = "https://soul-connection.fr/api/events"
    headers = {
        'accept': 'application/json',
        'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
        'Authorization' : f'Bearer {token}',
        #'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiJqZWFubmUubWFydGluQHNvdWwtY29ubmVjdGlvbi5mciIsIm5hbWUiOiJKZWFubmUiLCJzdXJuYW1lIjoiTWFydGluIiwiZXhwIjoxNzI3MzM4NDMyfQ.H1NsLsQjJiMPA97oYkslaPOwUA0PhE1LynUJQQOX0vQ',
    }
    response_token = requests.get(url_event, headers=headers)
    transform_request = response_token.json()
    check = Event.objects.all()
    for i in transform_request:
        event = Event()
        url_event_id = f"https://soul-connection.fr/api/events/{i.get('id')}"
        response_id = requests.get(url_event_id, headers=headers)
        
        try :
            get_response = response_id.json()
        except ValueError:
            print(f"Get_response: Error of JSON decodge: {url_event_id}")
            continue

        event.id = get_response.get("id")
        event.name = get_response.get("name")
        event.date = get_response.get("date")
        event.duration = get_response.get("duration")
        event.max_participants = get_response.get("max_participants")
        event.location_x = get_response.get("location_x")
        event.location_y = get_response.get("location_y")
        event.type = get_response.get("type")
        employee  = Employee.objects.get(id=get_response.get('employee_id'))
        event.employee = employee
        event.location_name = get_response.get("location_name")
        if event in check:
            continue
        event.save()
