from django.db import models
from datetime import datetime
from django.db import IntegrityError

class UserInfo(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=14)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.user_name
