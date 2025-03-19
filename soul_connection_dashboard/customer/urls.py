from django.urls import path
from .views import list_customers
from . import views

app_name = "customers"

urlpatterns = [
    path('list/', views.list_customers, name='customer'),
    path('compatibility/', views.customers_compatibility, name='compatibility'),
    path('create/', views.create_customers, name='customer-create'),
    path('detail/<int:id>/', views.detail_customers, name='customer-detail'),
    path('<int:id>/clothes/', views.customers_clothes, name='customer-clothes'),
    path('update/<int:id>/', views.update_customers, name='customer-update'),
    path('delete/<int:id>/', views.delete_customers, name='customer-delete'),
    path('<int:id>/clothes/create_clothes/', views.create_clothe, name='customer-create-clothes'),
    path('<int:customer_id>/clothes/update_clothes/<int:id>/', views.update_clothe, name='customer-update-clothes'),
    path('<int:customer_id>/clothes/delete_clothes/<int:id>', views.delete_clothe, name='customer-delete-clothes'),
]
