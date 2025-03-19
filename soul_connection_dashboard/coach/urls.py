from django.urls import path
from .views import list_employees
from . import views

app_name = "coachs"

urlpatterns = [
    path('list/', views.list_employees, name='coach'),
    path('create/', views.create_employee, name='coach-create'),
    path('detail/<int:id>/', views.detail_employee, name='coach-detail'),
    path('detail/<int:id>/message', views.create_message, name='message-create'),
    path('detail/<int:id>/messages/list', views.list_messages, name='message-list'),
    path('update/<int:id>/', views.update_employee, name='coach-update'),
    path('delete/<int:id>/', views.delete_employee, name='coach-delete'),
    #path('customer/<int:customer_id>/', views.customer_details, name='customer_details'),
]
