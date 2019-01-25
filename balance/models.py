from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Balance(models.Model):
    balance_count = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=80)

    def __str__(self):
        description = str(self.name) + '   ' + str(self.balance_count)
        return description

class Money_item(models.Model):
    date_of_item = models.DateField()
    change = models.DecimalField(max_digits=20, decimal_places=2)
    is_income = models.BooleanField(default=False)
    category = models.CharField(max_length=20)

    def __str__(self):
        des = 'date: ' + str(self.date_of_item)
        return des
