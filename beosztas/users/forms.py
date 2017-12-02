# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import DailyRequest, UsersDailyShift


class SignUpForm(UserCreationForm):
    username = forms.CharField(label=("Felhasználónév"), max_length=30)
    first_name = forms.CharField(label=("Keresztnév"), max_length=30)
    last_name = forms.CharField(label=("Vezetéknév"), max_length=30)
    email = forms.EmailField(max_length=254, help_text='Kötelező e-mail címet megadni')
    password1 = forms.CharField(label=("Jelszó"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Jelszó mégegyszer"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class DailyRequestForm(forms.ModelForm):
    class Meta:
        model = DailyRequest
        fields = ('day', 'shift', 'hours')


class UsersDailyShiftForm(forms.ModelForm):
    day = forms.CharField(disabled=True, label='')
    shift = forms.CharField(disabled=True, label='')
    hours = forms.CharField(disabled=True, label='')

    class Meta:
        model = UsersDailyShift
        fields = ('day', 'shift', 'hours')
