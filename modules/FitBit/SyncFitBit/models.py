from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
class FitBitAuthData(Document):
    access_token = StringField(max_length=500)
    refresh_token = StringField(max_length=500)
    expries_in = StringField(max_length=100)
    scope = StringField(max_length=100)
    user_id = StringField(max_length=100)
    token_type = StringField(max_length=100)

