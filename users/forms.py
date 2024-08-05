from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100, required=False)
    image = forms.ImageField(required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    pin_code = forms.CharField(max_length=10, required=False)
    favorite_food = forms.CharField(max_length=100, required=False)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']