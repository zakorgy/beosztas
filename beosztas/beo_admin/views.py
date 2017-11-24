# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRowForm, DailyShiftForm
from .models import DailyShift, UsersDailyShift, generate_daily_shift_requirements
import datetime

@login_required(login_url='home')
def create_shifts(request):
    today = datetime.date.today()
    (am, pm6, pm8) = generate_daily_shift_requirements(today)
    daily_shift = DailyShift.objects.filter(day=today).values()[0]
    daily_shift_form = DailyShiftForm(initial=daily_shift)
    for i in range(1,9):
        daily_shift_form.fields['am'+str(i)].choices = am
    for i in range(1,5):
        daily_shift_form.fields['pm6_'+str(i)].choices = pm8 + pm6
    for i in range(1,9):
        daily_shift_form.fields['pm8_'+str(i)].choices = pm8
    return render(request, 'create_shifts.html', {'daily_shift_form': daily_shift_form})

@login_required(login_url='home')
def manage_users(request):
    if request.method == 'POST':
        user_name_to_del = request.POST.get('username')
        user_to_del = User.objects.get(username=str(user_name_to_del))
        user_to_del.delete()
    user_row_forms = list()
    user_list = list(User.objects.filter(is_staff=False).values('username', 'first_name', 'last_name', 'email', 'id'))
    for user in user_list:
        user_row_form = UserRowForm(initial=user)
        user_row_forms.append(user_row_form)

    return render(request, 'manage_users.html', {'user_row_forms': user_row_forms})

@login_required(login_url='home')
def last_month_stat(request):
    return redirect('home')
