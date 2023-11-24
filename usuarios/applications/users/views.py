from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm
)
from django.views.generic.edit import(
    FormView,
    View,
)
from .models import User

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
        )
        return super(UserRegisterView, self).form_valid(form)
    
class LoginUser(FormView):
    template_name='users/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('home_app:panel')
    
    def form_valid(self, form):
        user=authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
    
class UpdatePasswordView(FormView):
    template_name='Users/update.html'
    form_class=UpdatePasswordForm
    success_url=reverse_lazy('users_app:user-login')
    
    def form_valid(self, form):
        usuario=self.request.user
        user=authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )
        if user:
            new_password=form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            
        logout(self.request)
        
        return super(UpdatePasswordView,self).form_valid(form)