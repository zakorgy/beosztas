# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
# Register your models here.

from .models import DailyRequest, UsersDailyShift

admin.site.register(DailyRequest)
admin.site.register(UsersDailyShift)
