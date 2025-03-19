from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class EmployeeManager(BaseUserManager):
    def create_employee(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_employee(email, password, **extra_fields)

class Employee(AbstractBaseUser, PermissionsMixin):
    def __str__(self):
        return f'{self.id} - {self.name} - {self.surname} - {self.email}'
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128, default="1234")
    birth_date = models.CharField(max_length=1000, blank=True)
    gender = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employees_image/')
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    last_login = models.DateTimeField(blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='employee_set',blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='employee_permissions_set', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeeManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

class Message(models.Model):
    def __str__(self):
        return f'{self.sender} - {self.receiver}'
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField(max_length=50000)