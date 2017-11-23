# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, WeeklyRequestForm, DailyRequestFormSet
from .models import DailyRequest, WeeklyRequest

# Create your views here.
from datetime import timedelta, date

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

@login_required(login_url='home')
def add_request(request):
    today = date.today()
    next_monday = today + timedelta(days=-today.weekday(), weeks=1)
    weekly_request_form = WeeklyRequestForm(initial={'week': WeeklyRequest.NEXT_WEEK})
    daily_request_forms = DailyRequestFormSet(initial=[
        {"day": str(next_monday) + ' (Hétfő)'},
        {"day": str(next_monday + timedelta(days=1)) + ' (Kedd)'},
        {"day": str(next_monday + timedelta(days=2)) + ' (Szerda)'},
        {"day": str(next_monday + timedelta(days=3)) + ' (Csütörtök)'},
        {"day": str(next_monday + timedelta(days=4)) + ' (Péntek)'},
        {"day": str(next_monday + timedelta(days=5)) + ' (Szombat)'},
        {"day": str(next_monday + timedelta(days=6)) + ' (Vasárnap)'},
    ])
    if request.method == 'POST':
        requested_week = request.POST.get('week')
        if int(requested_week) < WeeklyRequest.NEXT_WEEK:
            return render(request, 'add_request.html', {'weekly_request_form': weekly_request_form,
                                                        'daily_request_forms': daily_request_forms,
                                                        'request_error': 'Nem adhatsz meg ráérést visszamenőleg!'})
        weekly_request_form = WeeklyRequestForm(request.POST)
        if weekly_request_form.is_valid():
            weekly_request =weekly_request_form.save(commit=False)

            daily_request_forms = DailyRequestFormSet(request.POST, instance=weekly_request)
            if daily_request_forms.is_valid():
                weekly_request.user = request.user
                weekly_request.save()
                daily_request_forms.save()

                return redirect('home')
            else:
                print("asd")

    return render(request, 'add_request.html', {'weekly_request_form': weekly_request_form,
                                                'daily_request_forms': daily_request_forms,
                                                'request_error': {}})

@login_required(login_url='home')
def weekly_shift(request):
    return redirect('home')

@login_required(login_url='home')
def swap(request):
    return redirect('home')

@login_required(login_url='home')
def late_request(request):
    return redirect('home')

