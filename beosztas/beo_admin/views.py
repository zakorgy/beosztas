# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Shift

# Create your views here.

@login_required(login_url='home')
def create_shifts(request):
    return redirect('home')

@login_required(login_url='home')
def manage_users(request):
    return redirect('home')

@login_required(login_url='home')
def last_month_stat(request):
    return redirect('home')