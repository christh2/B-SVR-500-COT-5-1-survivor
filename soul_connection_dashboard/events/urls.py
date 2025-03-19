from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
      path('list/', views.list_event, name='event-list'),
      path('create_event/', views.create_events, name='event-create'),
      path('update_event/<int:id>/', views.update_events, name='update-event'),
      # path('delete_event/<int:id>/', views.delete_events, name='delete-event'),
]
