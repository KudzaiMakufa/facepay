from django.db import models

# Create your models here.

class Statement(models.Model):

    operation = models.CharField(default=0 , max_length=30)
    amount = models.DecimalField(default=0 , decimal_places=2,max_digits=65)
    date = models.DateField()
    account = models.CharField(default=0 , max_length=10)
