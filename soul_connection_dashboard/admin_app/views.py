from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import Employee
from customer.models import Customer
import requests
from encounters.models import Encounter
from events.models import Event
from collections import defaultdict
from django.contrib.auth.decorators import login_required
url_soul = "https://soul-connection.fr/api/employees/login"

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Group-Authorization': 'e0b26e39a7d57297568d65310365dce7',
    }
    response_token = requests.post(url_soul, json={'email': email, 'password': password}, headers=headers)
    if response_token.status_code == 200:
        response_to_it = response_token.json()
        stock_response = response_to_it["access_token"]
        return Response({'access_token': stock_response}, status=status.HTTP_200_OK)
    if response_token.status_code == 401:
        return Response({'invalid_credentials':'Invalid Email and Password combination.'})
    if response_token.status_code == 422:
        return Response({'Bad_token':'Token not found'})
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Vous êtes finalement connecté."})

def login_employee(request):
    message_error = ""
    if request.method == 'POST':
        form_log = LoginForm(request.POST)
        if form_log.is_valid():
            email = form_log.cleaned_data['email']
            password = form_log.cleaned_data['password']
            print("email=", email)
            print("password =", password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                for employee in Employee.objects.all():
                    if employee.email == email and employee.password == password:
                        if employee.work == "Coach":
                            return redirect('coachs:coach-detail', id=employee.id)
                        else:
                            return redirect('admin_app:dash')
            else :
                message_error = "Nom d'utilisateur ou mot de passe incorrect."
                print(message_error)
    else:
        form_log = LoginForm()
    context = {'form': form_log, 'messages_error': message_error}
    return render(request, 'admin_app/login.html', context)


@login_required(login_url='/employees/login/')
def acceuil(request):
    customers = Customer.objects.all()
    encounter = Encounter.objects.all()
    coach = Employee.objects.filter(work="Coach")
    nbr_employees = Employee.objects.all()
    nbr_coach = len(coach)
    events = Event.objects.all()
    source = {}
    for i in encounter:
        if i.source in source:
            source[i.source] += 1
        else:
            source[i.source] = 1
    
    take_year_month = defaultdict(lambda: defaultdict(list))
    final_year_month = [{}, {}, {}]
    z = 0
    for i in events:
        year, month, day = i.date.split('-')
        take_year_month[year][month].append(i)
    for year, months in take_year_month.items():
        print(f"{year}: {sum(len(i) for i in months.values())} events")
        final_year_month[z][year] = sum(len(i) for i in months.values())
        for month, e in sorted(months.items(), key=lambda a: int(a[0])):
            print(f"  {month}: {len(e)} events")
            final_year_month[z][month] = len(e)
        z = z + 1
    print(final_year_month)
    return render (request, 'admin_app/dash.html',
                   {'customers': customers,
                    'encounter': encounter,
                    'nbr_employees': nbr_employees,
                    'nbr_coach': nbr_coach,
                    'events': events,
                    'source': source,
                    'final_year_month': final_year_month,
                    })

def logout_employee(request):
    logout(request)
    return redirect('admin_app:login')