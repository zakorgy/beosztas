# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, DailyRequestForm, UsersDailyShiftForm
from .models import DailyRequest, UsersDailyShift, NEXT_WEEK

import datetime

TODAY = datetime.date.today()
NEXT_MONDAY = TODAY + datetime.timedelta(days=-TODAY.weekday(), weeks=1)


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

# Heti ráérés leadása vagy változtatása
@login_required(login_url='home')
def add_request(request):
    if request.method == 'POST':
        post_dict = dict(request.POST.lists())
        hours = post_dict['hours']
        shifts = post_dict['shift']
        days = post_dict['day']
        for i in range(0, 7):
            daily_request = DailyRequest.objects.get(user=request.user, day=days[i])
            daily_request.shift = shifts[i]
            daily_request.hours = hours[i]
            daily_request.save()
        return redirect('users:add_request')
    daily_request_forms = []
    for i in range(0, 7):
        day = NEXT_MONDAY + timedelta(days=i)
        daily_request = DailyRequest(user=request.user, day=day)
        if DailyRequest.objects.filter(user=request.user, day=day):
            daily_request = DailyRequest.objects.filter(user=request.user, day=day)[0]
        daily_request_form = DailyRequestForm(initial=daily_request.__dict__)
        daily_request.save()
        daily_request_forms.append(daily_request_form)
    return render(request, 'add_request.html', {'week': NEXT_WEEK,
                                                'daily_request_forms': daily_request_forms,
                                                'request_error': {}})


@login_required(login_url='home')
def late_request(request):
    return redirect('home')

#Az aktuális és a következő heti ráérése a usernek
@login_required(login_url='home')
def weekly_shift(request):
    current_weekly_shift = []
    next_weekly_shift = []
    for i in range(0, 7):
        day_nw = NEXT_MONDAY + timedelta(days=i)
        day_cw = day_nw - timedelta(days=7)
        if UsersDailyShift.objects.filter(user=request.user, day=day_cw):
            user_daily_shift = UsersDailyShift.objects.filter(user=request.user, day=day_cw)[0]
            user_daily_shift_dict = user_daily_shift.__dict__
            if user_daily_shift_dict['shift'].startswith('am'):
                user_daily_shift_dict['shift'] = 'délelőtt'
            else:
                user_daily_shift_dict['shift'] = 'délután'
            user_daily_shift_form = UsersDailyShiftForm(initial=user_daily_shift_dict)
            current_weekly_shift.append(user_daily_shift_form)
        if UsersDailyShift.objects.filter(user=request.user, day=day_nw):
            user_daily_shift = UsersDailyShift.objects.filter(user=request.user, day=day_nw)[0]
            user_daily_shift_dict = user_daily_shift.__dict__
            if user_daily_shift_dict['shift'].startswith('am'):
                user_daily_shift_dict['shift'] = 'délelőtt'
            else:
                user_daily_shift_dict['shift'] = 'délután'
            user_daily_shift_form = UsersDailyShiftForm(initial=user_daily_shift_dict)
            next_weekly_shift.append(user_daily_shift_form)
    return render(request, 'weekly_shift.html', {'week': NEXT_WEEK,
                                                 'current_weekly_shift': current_weekly_shift,
                                                 'next_weekly_shift': next_weekly_shift})


@login_required(login_url='home')
def swap(request):
    return redirect('home')

