from django import forms
from django.contrib.auth.models import User
from .models import Employee, Message

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'email', 'password','birth_date', 'gender', 'work', 'image', 'address', 'phone_number']
        widgets = {
            'password': forms.PasswordInput()
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['sender'].queryset = Employee.objects.filter(work="Coach")
        self.fields['receiver'].queryset = Employee.objects.filter(work="Coach")

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_joined', 'password']

    email = forms.EmailField(label='E-mail', required=True)
    first_name = forms.CharField(label='Nom', required=True)
    last_name = forms.CharField(label='Prénom', required=True)
    date_naissance = forms.DateField(label='Date de Naissance', required=True)
    genre = forms.ChoiceField(choices=[('masculin', 'Masculin'), ('feminin', 'Féminin'), ('autre', 'Autre')], label='Genre', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Mot de Passe', required=True)
    phone = forms.CharField(label='Numéro de Téléphone', required=True)
    adresse = forms.CharField(label='Adresse', required=True)
    work = forms.CharField(widget=forms.Textarea, label='Travail', required=False)
    image = forms.ImageField(label='Image', required=True)

