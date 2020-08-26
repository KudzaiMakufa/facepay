from django.db import models


# Create your models here.
class Transaction(models.Model):
    user_id = models.IntegerField(default=0)
    amount = models.DecimalField(default=0 , decimal_places=2,max_digits=65)
    date = models.DateField()
    account = models.CharField(default=0 , max_length=10)
    reference = models.CharField(default=0 ,max_length=100)

