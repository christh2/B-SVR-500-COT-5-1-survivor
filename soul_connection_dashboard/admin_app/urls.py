from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "admin_app"

urlpatterns = [
    path('login/', views.login_employee, name='login'),
    path('logout/', views.logout_employee, name='logout'),
    path('dash/', views.acceuil, name='dash'),  # Page d'accueil
    #path('customer/<int:customer_id>/', views.customer_details, name='customer_details'),
]
