# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, DailyRequestForm
from .models import DailyRequest

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def add_request(request, user_id):
    if request.method == 'POST':
        form = DailyRequestForm(request.POST)
        if form.is_valid():
            daily_req = form.save(commit=False)
            daily_req.user_id = user_id
            daily_req.save()
            return redirect('home')
    else:
        form = DailyRequestForm()
    return render(request, 'add_request.html', {'form': form})

