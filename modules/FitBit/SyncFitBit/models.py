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

