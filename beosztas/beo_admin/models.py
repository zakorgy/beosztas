# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from users.models import DailyRequest, WeeklyRequest

import datetime

# Create your models here.

class UsersDailyShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(max_length=20)
    shift = models.CharField(max_length=10)
    hours = models.SmallIntegerField

    def __str__(self):
        return "<Daily: %r Day: %r>" % (self.user, self.day)

    class Meta:
        unique_together = (("user", "day"),)

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

    @staticmethod
    def update_from_post(post):
        names = post.values()
        names.remove('Ü')
        if len(set(names)) != len(names):
            return False
        shift = DailyShift.objects.get(day=post.get('day'))
        shift.am1 = post.get('am1')
        shift.am2 = post.get('am2')
        shift.am3 = post.get('am3')
        shift.am4 = post.get('am4')
        shift.am5 = post.get('am5')
        shift.am6 = post.get('am6')
        shift.am7 = post.get('am7')
        shift.am8 = post.get('am8')

        shift.pm6_1 = post.get('pm6_1')
        shift.pm6_2 = post.get('pm6_2')
        shift.pm6_3 = post.get('pm6_3')
        shift.pm6_4 = post.get('pm6_4')

        shift.pm8_1 = post.get('pm8_1')
        shift.pm8_2 = post.get('pm8_2')
        shift.pm8_3 = post.get('pm8_3')
        shift.pm8_4 = post.get('pm8_4')
        shift.pm8_5 = post.get('pm8_5')
        shift.pm8_6 = post.get('pm8_6')
        shift.pm8_7 = post.get('pm8_7')
        shift.pm8_8 = post.get('pm8_8')
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
        name = request.week.user.first_name + " " + request.week.user.last_name
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
        print('am' + worker)
        AM_CHOICES += ((str(worker), str(worker)),)
    for i, worker in enumerate(possible_pm6_worker):
        print('pm6' + worker)
        PM6_CHOICES += ((str(worker), str(worker)),)
    for i, worker in enumerate(possible_pm8_worker):
        print('pm8' + worker)
        PM8_CHOICES += ((str(worker), str(worker)),)

    return (AM_CHOICES, PM6_CHOICES, PM8_CHOICES)
