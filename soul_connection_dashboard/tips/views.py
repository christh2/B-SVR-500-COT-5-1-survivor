# Create your views here.
from .models import Tip
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/employees/login')
def list_tips(request):
    tips = Tip.objects.all()
    return render(request,'tips/list_tip.html',{'tips': tips})
