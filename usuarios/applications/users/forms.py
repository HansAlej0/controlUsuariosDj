from django import forms
from .models import User

from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    password2=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )
    
    class Meta:
        model=User
        fields=(
            'username',
            'nombres',
            'apellidos',
            'email',
            'genero'
        )
        
    def clean_password2(self):
        if self.cleaned_data['password1']!=self.cleaned_data['password2']:
            self.add_error('password2','Las Contraseñas NO son iguales')
            
class LoginForm(forms.Form):
    username=forms.CharField(
        label='username',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'username',
                'style':'{margin:10px}',
            }
        )
    )
    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    def clean(self):
        cleaned_data=super(LoginForm, self).clean()
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Las credenciales no son correctas')
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
    password1=forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Actual'
            }
        )
    )
    password2=forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Nueva'
            }
        )
    )