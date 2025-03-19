# Create your views here.
from django.shortcuts import render
from .models import Employee, Message
from .forms import EmployeeForm, MessageForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/employees/login/')
def create_employee(request):
    messages_error = ""
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coachs:coach-detail', id=form.instance.id)
        else:
            messages_error = "Form is not valid"
            print("Les erreurs :", form.errors)
    else:
        form = EmployeeForm()
    return render(request,
                  'employee/create_employee.html',
                  {'form': form, 'messages_error': messages_error})

@login_required(login_url='/employees/login/')
def list_employees(request):
    employees = Employee.objects.all()
    if request.method == "GET":
        name = request.GET.get('name')
        surname = request.GET.get('surname')

        if name or surname:
            employees = Employee.objects.filter(name=name, surname=surname)

    coaches = Employee.objects.filter(work="Coach")
    nbr_coach = coaches.count()
    return render(request,'employee/list_employees.html',{'employees': employees, 'coaches': coaches, 'nbr_coach': nbr_coach})

@login_required(login_url='/employees/login/')
def detail_employee(request, id):
    employee = Employee.objects.get(id=id)
    customers = employee.clients.all()
    return render(request,
                  'employee/detail_employee.html',
                  {'employee': employee,
                   'customers': customers
                   })

@login_required(login_url='/employees/login/')
def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('coachs:coach-detail', id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request,
                  'employee/update_employee.html',
                  {'form': form, 'employee': employee})

@login_required(login_url='/employees/login/')
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        if employee.image:
            employee.image.delete()
        employee.delete()
        return redirect('coachs:coach')
    return render(request,
                  'employee/delete_employee.html',
                  {'employee': employee})

@login_required(login_url='/employees/login/')
def create_message(request, id):
    messages_error = ""
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coachs:message-list', id=employee.id)
        else:
            messages_error = "Form is not valid"
            print("Les erreurs :", form.errors)
    else:
        form = MessageForm()
    return render(request,
                  'employee/create_message.html',
                  {'form': form, 'messages_error': messages_error})

@login_required(login_url='/employees/login/')
def list_messages(request, id):
    employee = Employee.objects.get(id=id)
    my_messages = Message.objects.filter(receiver=employee)
    return render(request,
                  'employee/list_message.html',
                  {'my_messages': my_messages}) 


# def form(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Employé créé avec succès !")
#             return redirect('connexion')
#         else:
#             messages.error(request, "Erreur lors de la création de l'employé.")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'form.html', {'form': form})

