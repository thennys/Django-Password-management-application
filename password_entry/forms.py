from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from password_entry.models import PasswordEntry





class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username','password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    error_messages = {
        'invalid_login': 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['password'].label = False





class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['website_name', 'username']
