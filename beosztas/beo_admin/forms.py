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
    DEFAULT_CHOICES = (
        ('Ü', 'Üres'),
    )

    # the day of the shift
    day = forms.CharField()

    # Shifts before noon, these are all 8 hour shifts
    am1 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am2 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am3 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am4 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am5 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am6 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am7 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)
    am8 = forms.ChoiceField(label='___Délelőtt', choices=DEFAULT_CHOICES)

    # Afternoon shifts
    # 6 hour shifts
    pm6_1 = forms.ChoiceField(label='Délután (6)', choices=DEFAULT_CHOICES)
    pm6_2 = forms.ChoiceField(label='Délután (6)', choices=DEFAULT_CHOICES)
    pm6_3 = forms.ChoiceField(label='Délután (6)', choices=DEFAULT_CHOICES)
    pm6_4 = forms.ChoiceField(label='Délután (6)', choices=DEFAULT_CHOICES)

    # 8 hour shifts
    pm8_1 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_2 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_3 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_4 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_5 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_6 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_7 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)
    pm8_8 = forms.ChoiceField(label='Délután (8)', choices=DEFAULT_CHOICES)

#   def __init__(self, am_choices, pm6_choices, pm8_choices, *args, **kwargs):
#       super(DailyShiftForm, self).__init__(*args, **kwargs)
#       for i in range(1, 9):
#           self.fields['am' + str(i)].choices = am_choices
#       for i in range(1, 5):
#           self.fields['pm6_' + str(i)].choices = pm6_choices + pm8_choices
#       for i in range(1, 9):
#           self.fields['pm8_' + str(i)].choices = pm8_choices

    class Meta:
        model = DailyShift
        exclude = ('AM_CHOICES', 'PM6_CHOICES', 'PM8_CHOICES')

#    def clean(self):
#        names = []
#        print('Cleaned data = ' + str(dict(self.cleaned_data)))
#        for i in range(1,9):
#            name_am = str(self.cleaned_data.get('am'+str(i)))
#            name_pm8 = str(self.cleaned_data.get('pm8_'+str(i)))
#            if name_am != 'Ü':
#                names.append(name_am)
#            if name_pm8 != 'Ü':
#                names.append(name_pm8)
#        for i in range(1,5):
#            name_pm6 = str(self.cleaned_data.get('pm8_'+str(i)))
#            if name_pm6 != 'Ü':
#                names.append(name_pm6)
#
#        if len(names) != len(set(names)):
#            raise forms.ValidationError("Hiba! Egy név nem szerepelhet többször egy nap")

