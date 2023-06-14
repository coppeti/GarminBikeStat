import logging

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    )

from .forms import CustomUserCreationForm
from .models import CustomUser


# def login(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'login.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         print('POST')
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             api = Garmin(email, password)
#             print(api)
#             if Garmin(email, password):
#                 return redirect('home')
#             else:
#                 return render(request, 'test.html')
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'signup.html', {'form': form})


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'registration/signup.html', {'form': form})


class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'home'