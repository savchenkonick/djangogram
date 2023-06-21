from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from .models import DgUser
from django.contrib import messages
import time
from .forms import RegisterForm


def profile_view(*args, **kwargs):
    return HttpResponse("<h1>Hello world!</h1>")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('register')
            # return HttpResponseRedirect('/profile')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'profiles/register.html', {'form': form})