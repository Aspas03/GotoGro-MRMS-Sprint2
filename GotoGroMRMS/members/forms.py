# members/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile, Sale

# Form for registering new user
class UserRegisterForm(UserCreationForm):

    # Adding email field to registration form
    email = forms.EmailField(required=True)

    class Meta:
        # Specifies user model to use and fields to include in the form
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

# Form for updating user information
class UserUpdateForm(forms.ModelForm):

    # Specifies to use user model and fields to include in the form
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# Form to update profile model of a user
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        # Specifies profile model to use and the fields associated in this form
        model = Profile
        fields = ['address', 'phone_number', 'preferences']


class SaleUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Sale
        fields = ['item_name', 'purchase_quantity', 'total_price']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')