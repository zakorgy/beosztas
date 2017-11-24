# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from .models import DailyShift

class UserRowForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name')

class DailyShiftForm(forms.ModelForm):
    # the day of the shift
    day = forms.DateField(disabled=True)

#    AM_CHOICES = (
#        ('Ü', 'Üres'),
#    )
#
#    PM6_CHOICES = (
#        ('Ü', 'Üres'),
#    )
#
#    PM8_CHOICES = (
#        ('Ü', 'Üres'),
#    )

    # Shifts before noon, these are all 8 hour shifts
    am1 = forms.ChoiceField(label='DE')
    am2 = forms.ChoiceField(label="DE")
    am3 = forms.ChoiceField(label="DE")
    am4 = forms.ChoiceField(label="DE")
    am5 = forms.ChoiceField(label="DE")
    am6 = forms.ChoiceField(label="DE")
    am7 = forms.ChoiceField(label="DE")
    am8 = forms.ChoiceField(label="DE")

    # Afternoon shifts
    # 6 hour shifts
    pm6_1 = forms.ChoiceField(label='DU 6')
    pm6_2 = forms.ChoiceField(label='DU 6')
    pm6_3 = forms.ChoiceField(label='DU 6')
    pm6_4 = forms.ChoiceField(label='DU 6')

    # 8 hour shifts
    pm8_1 = forms.ChoiceField(label='DU 8')
    pm8_2 = forms.ChoiceField(label='DU 8')
    pm8_3 = forms.ChoiceField(label='DU 8')
    pm8_4 = forms.ChoiceField(label='DU 8')
    pm8_5 = forms.ChoiceField(label='DU 8')
    pm8_6 = forms.ChoiceField(label='DU 8')
    pm8_7 = forms.ChoiceField(label='DU 8')
    pm8_8 = forms.ChoiceField(label='DU 8')


    class Meta:
        model = DailyShift
        exclude = ('AM_CHOICES', 'PM6_CHOICES', 'PM8_CHOICES')

    def clean(self):
        names = []
        for i in range(1,9):
            name_am = str(self.fields['am'+str(i)])
            name_pm8 = str(self.fields['pm8_'+str(i)])
            if name_am != 'Üres':
                names.append(name_am)
            if name_pm8 != 'Üres':
                names.append(name_pm8)
        for i in range(1,5):
            name_pm6 = str(self.fields['pm8_'+str(i)])
            if name_pm6 != 'Üres':
                names.append(name_pm6)

        if len(names) != len(set(names)):
            raise forms.ValidationError("Hiba! Egy név nem szerepelhet többször egy nap")

