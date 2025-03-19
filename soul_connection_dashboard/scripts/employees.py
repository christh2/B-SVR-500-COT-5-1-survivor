import os
import django
import requests
from rest_framework import status
from rest_framework.response import Response
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
    url_customer = "https://soul-connection.fr/api/employees"
    headers = {
        'accept': 'application/json',
        'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
        'Authorization' : f'Bearer {token}',
        #'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiJqZWFubmUubWFydGluQHNvdWwtY29ubmVjdGlvbi5mciIsIm5hbWUiOiJKZWFubmUiLCJzdXJuYW1lIjoiTWFydGluIiwiZXhwIjoxNzI3MzM4NDMyfQ.H1NsLsQjJiMPA97oYkslaPOwUA0PhE1LynUJQQOX0vQ',
    }
    response_token = requests.get(url_customer, headers=headers)
    transform_request = response_token.json()
    check = Employee.objects.all()
    for i in transform_request:
        employee = Employee()
        
        url_customer_id = f"https://soul-connection.fr/api/employees/{i.get('id')}"
        url_customer_image = f"https://soul-connection.fr/api/employees/{i.get('id')}/image"
        
        response_image = requests.get(url_customer_image, headers=headers)
        response_id = requests.get(url_customer_id, headers=headers)
        
        get_response = response_id.json()
        
        employee.id = get_response.get("id")
        employee.email = get_response.get("email")
        employee.name = get_response.get("name")
        employee.surname = get_response.get("surname")
        employee.birth_date = get_response.get("birth_date")
        employee.gender = get_response.get("gender")
        employee.work = get_response.get("work")

        image_name = f"employee_{employee.id}.png" 
        employee.image.save(image_name, ContentFile(response_image.content))
        
        if employee in check:
            continue
        employee.save()
