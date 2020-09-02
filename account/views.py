from django.shortcuts import render
from django.http import HttpResponse
from custom.balance import Balance 

# Create your views here.
def balance(request):

    account = Balance()

    
    amount = account.check_balance(request.user.username).amount

    context = {
            'amount' : amount
    }

    return render(request , 'account/balance.html' , context)
