# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
