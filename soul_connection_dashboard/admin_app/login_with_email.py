from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Employee

class EmailLogin(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Employee.objects.get(email=email)
            #if user.check_password(password):
            if user.password == password:
                return user
        except Employee.DoesNotExist:
            return None
        return None
    
    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None