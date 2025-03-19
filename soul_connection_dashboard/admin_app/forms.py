from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', required=True)

