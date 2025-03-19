import os
import django
import requests
from rest_framework import status
from rest_framework.response import Response
from customer.models import Customer, Payment, Clothe
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
        print("Invalid token\n\n\n")
        return
    url_customer = "https://soul-connection.fr/api/customers"
    headers = {
        'accept': 'application/json',
        'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
        'Authorization' : f'Bearer {token}',
        #'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiJqZWFubmUubWFydGluQHNvdWwtY29ubmVjdGlvbi5mciIsIm5hbWUiOiJKZWFubmUiLCJzdXJuYW1lIjoiTWFydGluIiwiZXhwIjoxNzI3MzM4NDMyfQ.H1NsLsQjJiMPA97oYkslaPOwUA0PhE1LynUJQQOX0vQ',
    }
    response_token = requests.get(url_customer, headers=headers)
    transform_request = response_token.json()
    
    check_customers = Customer.objects.all()
    check_payments = Payment.objects.all()
    check_clothes = Clothe.objects.all()

    for i in transform_request:
        customer = Customer()
        
        url_customer_id = f"https://soul-connection.fr/api/customers/{i.get('id')}"
        url_customer_image = f"https://soul-connection.fr/api/customers/{i.get('id')}/image"
        url_payment = f"https://soul-connection.fr/api/customers/{i.get('id')}/payments_history"
        url_clothes = f"https://soul-connection.fr/api/customers/{i.get('id')}/clothes"
        
        response_image = requests.get(url_customer_image, headers=headers)
        response_id = requests.get(url_customer_id, headers=headers)
        response_payment = requests.get(url_payment, headers=headers)
        response_clothes = requests.get(url_clothes, headers=headers)
        
        try :
            get_response = response_id.json()
        except ValueError:
            print(f"Get_response: Error of JSON decodge: {url_customer_id}")
            continue

        customer.id = get_response.get("id")
        customer.email = get_response.get("email")
        customer.name = get_response.get("name")
        customer.surname = get_response.get("surname")
        customer.birth_date = get_response.get("birth_date")
        customer.gender = get_response.get("gender")
        customer.description = get_response.get("description")
        customer.astrological_sign = get_response.get("astrological_sign")
        customer.phone_number = get_response.get("phone_number")
        customer.address = get_response.get("address")
        image_name = f"customer_{customer.id}.png" 
        customer.image.save(image_name, ContentFile(response_image.content))
        if customer not in check_customers:
            customer.save()

        try :
            get_payments = response_payment.json()
        except ValueError:
            print(f"Get_payments: Error of JSON decodge: {url_payment}")
            get_payments = []

        for i in get_payments:
            payment = Payment()
            payment.customer = customer
            payment.id = i.get("id")
            payment.date = i.get("date")
            payment.payment_method = i.get("payment_method")
            payment.amount = i.get("amount")
            payment.comment = i.get("comment")
            if payment not in check_payments:
                payment.save()

        try :
            get_clothes = response_clothes.json()
        except ValueError:
            print(f"Get_clothes: Error of JSON decodge: {url_clothes}")
            get_clothes = []
        
        for i in get_clothes:
            clothes = Clothe()
            clothes.customer = customer
            clothes.id = i.get("id")
            clothes.type = i.get("type")
            url_clothe_image = f"https://soul-connection.fr/api/clothes/{i.get("id")}/image"
            response_clothes = requests.get(url_clothe_image, headers=headers)
            image_name = f"customer_clothe_{customer.id}_{i.id}.png"
            clothes.image.save(image_name, ContentFile(response_clothes.content))
            if clothes not in check_clothes:
                clothes.save()