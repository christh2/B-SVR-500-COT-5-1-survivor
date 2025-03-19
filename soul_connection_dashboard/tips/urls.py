from django.urls import path
from . import views

app_name = "tips"

urlpatterns = [
     path('list/', views.list_tips, name='tips-list'),
]
