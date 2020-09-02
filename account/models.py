from django.db import models

# Create your models here.
class Account(models.Model):
    
    amount = models.DecimalField(default=0 , decimal_places=2,max_digits=65)
    account = models.CharField(default=0 , max_length=10)
 
