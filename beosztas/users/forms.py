# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import DailyRequest, WeeklyRequest, LateRequest


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

class WeeklyRequestForm(forms.ModelForm):
    class Meta:
        model = WeeklyRequest
        fields = ('week',)
        labels = {
            'week': ('Hét'),
        }

class CustomDailyRequestFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(CustomDailyRequestFormSet, self).clean()

DailyRequestFormSet = forms.inlineformset_factory(WeeklyRequest,
                                                  DailyRequest,
                                                  formset=CustomDailyRequestFormSet,
                                                  fields=['day', 'shift','hours'],
                                                  extra=7)

class CustomLateRequestFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(CustomLateRequestFormSet, self).clean()

LateRequestFormSet = forms.inlineformset_factory(WeeklyRequest,
                                                 LateRequest,
                                                 formset=CustomLateRequestFormSet,
                                                 fields=['day', 'shift','hours'],
                                                 extra=7)
