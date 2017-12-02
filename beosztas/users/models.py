# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

NEXT_WEEK = datetime.date.today().isocalendar()[1] + 1


class DailyRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(max_length=20)
    SHIFT_CHOICES = (
        ('DE', 'délelőtt'),
        ('DU', 'délután'),
        ('NO', 'nem'),
    )
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, default='NO')
    HOUR_CHOICES = (
        (6, 6),
        (8, 8),
    )
    hours = models.SmallIntegerField(choices=HOUR_CHOICES, default=6)

    def __str__(self):
        return "<User: %r Day: %r>" % (self.user, self.day)

    class Meta:
        unique_together = (("user", "day"),)


class UsersDailyShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(max_length=20)
    shift = models.CharField(max_length=10)
    hours = models.IntegerField(default=8)

    def __str__(self):
        return "<Daily: %r Day: %r>" % (self.user, self.day)

    class Meta:
        unique_together = (("user", "day"),)


    #UsersDailyShift létrehozása DailyShift alapján, illetve mentése az adatbázisba
    @staticmethod
    def create_from_daily_shift(daily_shift, day, shift_str):
        name = getattr(daily_shift, shift_str)
        if name != 'Ü' and name != 'Üres':
            first_name, last_name = name.split(" ")
            # TODO: Ez így nem túl jó megoldás, ha 2 embernek ugyanaz a neve, akkor nem tudjuk melyiket veszi ki.
            user = User.objects.filter(first_name=first_name, last_name=last_name)[0]
            users_daily_shift = UsersDailyShift(user=user, day=day, shift=shift_str)
            # Ha valakit már dolgozik ebben a műszakban, akkor töröljük
            if UsersDailyShift.objects.filter(day=day, shift=shift_str):
                users_daily_shift2 = UsersDailyShift.objects.get(day=day, shift=shift_str)
                users_daily_shift2.delete()
            users_daily_shift.save()