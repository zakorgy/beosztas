# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class DailyRequest(models.Model):
    # foreign key a userhez
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # a nap dátuma amihez tartozik a rekord
    day = models.DateField(max_length=20, default=now)
    # dologzik-e az adott napon
    is_working = models.BooleanField(default=False)
    # reggeli vagy delutani muszak
    SHIFT_CHOICES = (
        ('DE', 'délelőtt'),
        ('DU', 'délután'),
    )
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, default='DE')
    # 6 vagy 8 oras muszak
    HOUR_CHOICES = (
        (6, 6),
        (8, 8),
    )
    hours = models.SmallIntegerField(choices=HOUR_CHOICES, default=6)
    class Meta:
        unique_together = (('user', 'day'))
