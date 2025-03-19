from django.shortcuts import render

# Create your views here.
from .models import Event
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import EventForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/employees/login')
def list_event(request):
    events = Event.objects.all()
    event_tab = []
    for i in events:
        event_tab.append(i)
    return render(request, 'events/list_events.html', {'event_tab': event_tab})

@login_required(login_url='/employees/login')
def create_events(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:event-list')
        else:
             print("Les erreurs :", form.errors)
    else:
        form = EventForm()
    return render(request,'events/create_events.html',{'form': form})

@login_required(login_url='/employees/login')
def update_events(request, id):
    events = Event.objects.get(id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=events)
        if form.is_valid():
            events = form.save()
            return redirect('events:event-list')
    else:
        form = EventForm(instance=events)
    return render(request,'events/update_events.html',{'form': form, 'events': events})

# @login_required(login_url='/employees/login')
# @permission_required("", login_url="")
# def delete_events(request, id):
#     events = Event.objects.get(id=id)
#     if request.method == 'POST':
#         if events.location_name:
#             events.delete()
#         events.delete()
#         return redirect('events:event-list')
#     return render(request,'events/delete_events.html',{'events': events})