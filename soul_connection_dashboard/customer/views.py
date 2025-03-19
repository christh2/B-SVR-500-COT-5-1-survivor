# Create your views here.
from django.db.models.fields import return_None
from django.shortcuts import render, get_object_or_404
from .models import Customer, Clothe, Payment
from encounters.models import Encounter
from .forms import CustomerForm, CompatibilityForm, ClothingItemForm
from admin_app.models import Meeting
from datetime import datetime
from django.shortcuts import redirect
from .astro import check_client_compatibility
from django.contrib.auth.decorators import login_required

@login_required(login_url='/employees/login/')
def create_customers(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers:customer-detail', id=form.instance.id)
        else:
             print("Les erreurs :", form.errors)
    else:
        form = CustomerForm()
    return render(request,
                  'customer/create_customers.html',
                  {'form': form})

@login_required(login_url='/employees/login/')
def list_customers(request):
    customers = Customer.objects.all()
    if request.method == "GET":
        name = request.GET.get('name')
        surname = request.GET.get('surname')
        if name or surname:
            customers = Customer.objects.filter(name=name, surname=surname)
    payment = []
    for i in customers:
        payment.append(i.payment_set.all())
    return render(request,'customer/list_customers.html',{'customers': customers,'payment': payment})

@login_required(login_url='/employees/login/')
def detail_customers(request, id):
    customers = Customer.objects.get(id=id)
    payment = customers.payment_set.all()
    meetings = customers.encounters.all()
    positives = 0; progess = 0
    for i in meetings:
        if i.rating >= 4:
            positives += 1
        else:
            progess += 1
    def sorte_date(meetings):
        try:
            return datetime.strptime(meetings.date, "%Y-%m-%d")
        except ValueError:
            return None
    meetings = sorted(meetings, key=sorte_date, reverse=True)
    return render(request,
                  'customer/detail_customers.html',
                  {'customers': customers,
                   'payment': payment,
                   'meetings': meetings,
                   'positives': positives,
                   'progess': progess,
                   })

@login_required(login_url='/employees/login/')
def update_customers(request, id):
    customers = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customers)
        if form.is_valid():
            customers = form.save()
            return redirect('customers:customer-detail', id=customers.id)
    else:
        form = CustomerForm(instance=customers)
    return render(request,
                  'customer/update_customers.html',
                  {'form': form, 'customers': customers})

@login_required(login_url='/employees/login/')
def delete_customers(request, id):
    customers = Customer.objects.get(id=id)
    if request.method == 'POST':
        if customers.image:
            customers.image.delete()
        customers.delete()
        return redirect('customers:customer')
    return render(request,
                  'customer/delete_customers.html',
                  {'customers': customers})

@login_required(login_url='/employees/login/')
def customers_compatibility(request):
    percentage = 0
    if request.method == 'POST':
        form_log = CompatibilityForm(request.POST)
        if form_log.is_valid():
            first_client = form_log.cleaned_data['first_client']
            second_client = form_log.cleaned_data['second_client']
            info_first_client = Customer.objects.get(email=first_client)
            info_second_client = Customer.objects.get(email=second_client)
            percentage = check_client_compatibility(info_first_client.astrological_sign, info_second_client.astrological_sign)
            print("email : ", info_first_client.email, "astrological_sign : ", info_first_client.astrological_sign)
            print("email : ", info_second_client.email, "astrological_sign : ", info_second_client.astrological_sign)
            print("percentage : ", percentage)
    else:
        form_log = CompatibilityForm()
    context = {'form_log': form_log, 'percentage': percentage}
    return render(request, 'customer/compatibility.html', context)

@login_required(login_url='/employees/login/')
def customers_clothes(request, id):
    customer = Customer.objects.get(id=id)
    clothe = customer.clothe_set.all()
    if request.method == "POST":
        ids = request.POST.get('ids')
        if ids:
            id_list = [int(i.strip()) for i in ids.split(',')]
            clothe = clothe.filter(id__in=id_list)
    return render(request, 'customer/customers_clothes.html', {'customer': customer, 'clothe': clothe})

@login_required(login_url='/employees/login/')
def create_clothe(request, id):
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers:customer-clothes', id=id)
        else:
             print("Les erreurs :", form.errors)
    else:
        form = ClothingItemForm()
    return render(request,'customer/create_clothes.html',{'form': form})

@login_required(login_url='/employees/login/')
def update_clothe(request, customer_id, id):
    cloth = Clothe.objects.get(id=id)
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, request.FILES, instance=cloth)
        if form.is_valid():
            cloth = form.save()
            return redirect('customers:customer-clothes', id=customer_id)
    else:
        form = ClothingItemForm(instance=cloth)
    return render(request,'customer/update_clothes.html',{'form': form, 'cloth': cloth})

@login_required(login_url='/employees/login/')
def delete_clothe(request, customer_id, id):
    cloth = Clothe.objects.get(id=id)
    if request.method == 'POST':
        if cloth.image:
            cloth.image.delete()
        cloth.delete()
        return redirect('customers:customer-clothes', id=customer_id)
    return render(request, 'customer/delete_clothe.html', {'cloth': cloth})
