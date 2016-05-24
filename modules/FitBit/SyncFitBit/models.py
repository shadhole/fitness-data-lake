from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FitBitData(models.Model):
    all_data = models.CharField(max_length=300)