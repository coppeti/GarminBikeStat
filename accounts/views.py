from django.shortcuts import render

from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'base.html')


def login_view(request):
    form = CustomUserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    return render(request, 'login_view.html', {'form': form})