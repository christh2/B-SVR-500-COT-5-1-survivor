from django import forms
from .models import Customer, Clothe, Payment
from coach.models import Employee

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['coach'].queryset = Employee.objects.filter(work="Coach")

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

class CompatibilityForm(forms.Form):
    first_client = forms.EmailField(label='Email', required=True)
    second_client = forms.EmailField(label='Email', required=True)

class ClothingForm(forms.Form):
    my_id = forms.IntegerField()
    id_clothes = forms.IntegerField()
    type = forms.CharField(max_length=200)
    image = forms.ImageField()

class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = Clothe
        fields = "__all__"
