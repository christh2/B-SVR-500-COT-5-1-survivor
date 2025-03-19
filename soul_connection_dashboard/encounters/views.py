# Create your views here.
from django.shortcuts import render
from .models import Encounter
from .forms import EncounterForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/employees/login')
def create_encounter(request):
    if request.method == 'POST':
        form = EncounterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('encounter-detail', id=form.instance.id)
    else:
        form = EncounterForm()
    return render(request,
                  'encounter/create_encounter.html',
                  {'form': form})

@login_required(login_url='/employees/login')
def list_encounter(request):
    encounter = Encounter.objects.all()
    return render(request,
                  'encounter/list_encounter.html',
                  {'encounter': encounter})

@login_required(login_url='/employees/login')
def detail_encounter(request, id):
    encounter = Encounter.objects.get(id=id)
    return render(request,
                  'encounter/detail_encounter.html',
                  {'encounter': encounter})

@login_required(login_url='/employees/login')
def update_encounter(request, id):
    encounter = Encounter.objects.get(id=id)
    if request.method == 'POST':
        form = EncounterForm(request.POST, instance=encounter)
        if form.is_valid():
            encounter = form.save()
            return redirect('encounter-detail', id=encounter.id)
    else:
        form = EncounterForm(instance=encounter)
    return render(request,
                  'encounter/update_encounter.html',
                  {'form': form, 'encounter': encounter})

@login_required(login_url='/employees/login')
def delete_encounter(request, id):
    encounter = Encounter.objects.get(id=id)
    if request.method == 'POST':
        if encounter.image:
            encounter.image.delete()
        encounter.delete()
        return redirect('encounter-list')
    return render(request,
                  'encounter/delete_encounter.html',
                  {'encounter': encounter})
