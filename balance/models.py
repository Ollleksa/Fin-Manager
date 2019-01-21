from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Balance(models.Model):
    balance_count = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    name = models.CharField(max_length=80, default=User.username)

    def __str__(self):
        return self.user_name + ':   ' + str(self.balance_count)
