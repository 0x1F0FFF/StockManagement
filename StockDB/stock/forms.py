from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Location, InventoryItem

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class InventoryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), initial=0)

    class Meta:
        model = InventoryItem
        fields = ['part', 'name', 'quantity', 'category', 'location']
