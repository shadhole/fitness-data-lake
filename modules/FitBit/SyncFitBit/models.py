from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FitBitAuthData(models.Model):
    access_token = models.CharField(max_length=500)
    refresh_token = models.CharField(max_length=500)
    expries_in = models.CharField(max_length=100)
    scope = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    token_type = models.CharField(max_length=100)

class UserProfile(models.Model):
    full_name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    height = models.CharField(max_length=20)
    height_unit = models.CharField(max_length=10)
    weight = models.CharField(max_length=5)
    weight_unit = models.CharField(max_length=5)
    country = models.CharField(max_length=25)
    fitbit_id = models.CharField(max_length=20)
    def __str__(self):
        return self.fitbit_id