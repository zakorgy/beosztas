# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
# Register your models here.

from .models import WeeklyRequest, DailyRequest

admin.site.register(WeeklyRequest)
admin.site.register(DailyRequest)