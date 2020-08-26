from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.IntegerField(default=0)
    amount = models.DecimalField(default=0 , decimal_places=2,max_digits=65)
 
