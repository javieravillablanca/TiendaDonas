from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre y Apellido',
        required=True,
        min_length=5,
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca sus datos'})
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca su email'})
    )
    message = forms.CharField(
        label='Mensaje',
        required=True,
        max_length=90,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba aquí su mensaje...', 'rows': 5})
    )
    contact_type = forms.ChoiceField(
        label='Tipo de contacto',
        choices=[(0, 'Queja por un producto'), (1, 'Felicitaciones')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subscription = forms.BooleanField(
        label='Suscribirme para más información',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input','id':'checkboxDiv'})
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'contact_type', 'subscription']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input is-primary', 'placeholder': 'Correo Electrónico'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'input is-primary'}),
            'password2': forms.PasswordInput(attrs={'class': 'input is-primary'}),
            'username': forms.TextInput(attrs={'class': 'input is-primary', 'placeholder': 'Javiera'})
        }
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña'
        }
