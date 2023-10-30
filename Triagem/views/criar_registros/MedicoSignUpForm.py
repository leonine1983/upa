from django import forms
from django.contrib.auth.models import User


# xxxxxxxxxxxxxxxxx CRIA USUARIOS ENFERMAGE E TEC XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class MedicoSignUpForm(forms.ModelForm):    
    telefone = forms.CharField(max_length=20)
    data_nascimento = forms.DateField()

    endereco = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite o nome da rua'}), label='Rua')
    crm = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o nº COREN'}), label="nº COREN")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'crm', 'endereco')    
