from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Shift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(max_length=20)
    shift = models.CharField(max_length=10)
    hours = models.SmallIntegerField

    def __str__(self):
        return "<Daily: %r Day: %r>" % (self.user, self.day)

    class Meta:
        unique_together = (("user", "day"),)
