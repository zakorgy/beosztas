# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
# Register your models here.

from .models import DailyShift, UsersDailyShift

admin.site.register(DailyShift)
admin.site.register(UsersDailyShift)