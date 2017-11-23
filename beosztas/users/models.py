# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime

# Create your models here.

class WeeklyRequest (models.Model):
    NEXT_WEEK = datetime.date.today().isocalendar()[1] + 1
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.SmallIntegerField(primary_key=True)

    def __str__(self):
        return "<Week: %r  User: %r>" % (self.week, self.user)

    class Meta:
        unique_together = (("user", "week"),)

class DailyRequest(models.Model):
    # foreign key a userhez
    week = models.ForeignKey(WeeklyRequest, on_delete=models.CASCADE)
    # a nap dátuma amihez tartozik a rekord
    day = models.DateField(max_length=20)
    # reggeli vagy delutani muszak
    SHIFT_CHOICES = (
        ('DE', 'délelőtt'),
        ('DU', 'délután'),
        ('NO', 'nem'),
    )
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, default='NO')
    # 6 vagy 8 oras muszak
    HOUR_CHOICES = (
        (6, 6),
        (8, 8),
    )
    hours = models.SmallIntegerField(choices=HOUR_CHOICES, default=6)


    def __str__(self):
        return "<Daily: %r Day: %r>" % (self.week, self.day)

    class Meta:
        unique_together = (("week", "day"),)

class LateRequest(models.Model):
    # foreign key a userhez
    week = models.ForeignKey(WeeklyRequest, on_delete=models.CASCADE)
    # a nap dátuma amihez tartozik a rekord
    day = models.DateField(max_length=20)
    # reggeli vagy delutani muszak
    SHIFT_CHOICES = (
        ('DE', 'délelőtt'),
        ('DU', 'délután'),
        ('NO', 'nem'),
    )
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, default='NO')
    # 6 vagy 8 oras muszak
    HOUR_CHOICES = (
        (6, 6),
        (8, 8),
    )
    hours = models.SmallIntegerField(choices=HOUR_CHOICES, default=6)

    def __str__(self):
        return "<Daily: %r Day: %r>" % (self.week, self.day)

    class Meta:
        unique_together = (("week", "day"),)
