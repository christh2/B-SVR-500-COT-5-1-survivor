from django.urls import path
from . import views

app_name = "encounters"

urlpatterns = [
    path('list/', views.list_encounter, name='encounter'),
    path('create/', views.create_encounter, name='encounter-create'),
    path('detail/<int:id>/', views.detail_encounter, name='encounter-detail'),
    path('update/<int:id>/', views.update_encounter, name='encounter-update'),
    path('delete/<int:id>/', views.delete_encounter, name='encounter-delete'),
    path('customer/<int:id>/', views.delete_encounter, name='encounter-customer'),
]
