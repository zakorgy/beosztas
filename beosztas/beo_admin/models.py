# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from users.models import DailyRequest
import re


NAME_REGEX = r'^([A-Z]([a-záéúőóüö.]{1,}\s?)){2,}$'
NAME_REGEX = re.compile(NAME_REGEX, re.IGNORECASE)


class DailyShift(models.Model):
    # the day of the shift
    day = models.DateField(unique=True)

    # Shifts before noon, these are all 8 hour shifts
    am1 = models.CharField(max_length=30, default='Üres')
    am2 = models.CharField(max_length=30, default='Üres')
    am3 = models.CharField(max_length=30, default='Üres')
    am4 = models.CharField(max_length=30, default='Üres')
    am5 = models.CharField(max_length=30, default='Üres')
    am6 = models.CharField(max_length=30, default='Üres')
    am7 = models.CharField(max_length=30, default='Üres')
    am8 = models.CharField(max_length=30, default='Üres')

    # Afternoon shifts
    # 6 hour shifts
    pm6_1 = models.CharField(max_length=30, default='Üres')
    pm6_2 = models.CharField(max_length=30, default='Üres')
    pm6_3 = models.CharField(max_length=30, default='Üres')
    pm6_4 = models.CharField(max_length=30, default='Üres')

    # 8 hour shifts
    pm8_1 = models.CharField(max_length=30, default='Üres')
    pm8_2 = models.CharField(max_length=30, default='Üres')
    pm8_3 = models.CharField(max_length=30, default='Üres')
    pm8_4 = models.CharField(max_length=30, default='Üres')
    pm8_5 = models.CharField(max_length=30, default='Üres')
    pm8_6 = models.CharField(max_length=30, default='Üres')
    pm8_7 = models.CharField(max_length=30, default='Üres')
    pm8_8 = models.CharField(max_length=30, default='Üres')

    def has_empty_field(self):
        for i in range(1, 9):
            am_str = 'am' + str(i)
            if getattr(self, am_str) == 'Ü':
                return (True, 'délelőttös')
            pm8_str = 'pm8_' + str(i)
            if getattr(self, pm8_str) == 'Ü':
                return (True, 'délután nyolcas')
            if i < 5:
                pm6_str = 'pm6_' + str(i)
                if getattr(self, pm6_str) == 'Ü':
                    return (True, 'délután hatos')
        return (False, '')

    def has_empty_field_mock(self):
        return (False, '')


def update_from_post(post):
    names = list()
    for name in list(post.values()):
        if name != 'Ü' and NAME_REGEX.match(name):
            names.append(name)
    #print('NAMES: ' + str(names))
    if len(set(names)) != len(names):
        return False
    shift = DailyShift.objects.get(day=post.get('day'))
    for i in range(1, 9):
        am_str = 'am' + str(i)
        setattr(shift, am_str, post.get(am_str))
        pm8_str = 'pm8_' + str(i)
        setattr(shift, pm8_str, post.get(pm8_str))
        if i < 5:
            pm6_str = 'pm6_' + str(i)
            setattr(shift, pm6_str, post.get(pm6_str))
    shift.save()
    return True


def generate_daily_shift_requirements(day):
    daily_shift = DailyShift()
    daily_shift.day = day
    if DailyShift.objects.filter(day=day):
            daily_shift = DailyShift.objects.get(day=day)
    requests_for_this_day = DailyRequest.objects.exclude(shift='nem').filter(day=day)
    #print( str(requests_for_this_day))
    possible_am_worker = list()
    possible_pm6_worker = list()
    possible_pm8_worker = list()
    for request in requests_for_this_day:
        name = request.user.first_name + " " + request.user.last_name
        #print('Userd name:' + user_name)
        print("SHIFT: " + str(request.shift))
        if request.shift == 'DE':
            possible_am_worker.append(name)
        elif request.shift == 'DU' and request.shift == 6:
            possible_pm6_worker.append(name)
        else:
            possible_pm8_worker.append(name)
    daily_shift.save()

    AM_CHOICES = (
        ('Ü', 'Üres'),
    )

    PM6_CHOICES = (
    )

    PM8_CHOICES = (
        ('Ü', 'Üres'),
    )

    for i, worker in enumerate(possible_am_worker):
        #print('am' + worker)
        AM_CHOICES += ((str(worker), str(worker)),)
    for i, worker in enumerate(possible_pm6_worker):
        #print('pm6' + worker)
        PM6_CHOICES += ((str(worker), str(worker)),)
    for i, worker in enumerate(possible_pm8_worker):
        #print('pm8' + worker)
        PM8_CHOICES += ((str(worker), str(worker)),)

    return (AM_CHOICES, PM6_CHOICES, PM8_CHOICES)
