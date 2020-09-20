from django.shortcuts import render,redirect
from django.http import HttpResponse
from custom.balance import Balance 
from .forms import DepositForm
from decimal import *
import datetime
from django.contrib import messages

# Create your views here.
def balance(request):

    account = Balance()

    
    amount = account.check_balance(request.user.username).amount

    context = {
            'amount' : amount
    }

    return render(request , 'account/balance.html' , context)

def deposit(request):

    balance = Balance()
   

    if request.method == "POST":

        account = request.POST.get('account') 
        amount = Decimal(request.POST.get('amount')) 
        # print(request.POST.get('account'))
       
        
        balance.transferin(account = account , amount = amount)
        

        # from depositer
        statementdata = {
                    
                    "operation":"Deposited Funds",
                    "amount":amount ,
                    "date":datetime.datetime.now() ,
                    "account": request.user.username ,
                }
        balance.statementcreate(statementdata)

        # to receiver 
        statementdata = {
                    
                    "operation":"Received Funds",
                    "amount":amount ,
                    "date":datetime.datetime.now() ,
                    "account": account ,
        }
        balance.statementcreate(statementdata)

        messages.add_message(request, messages.INFO, ' Deposit successful')
        return redirect('/account/deposit/')
    
#     amount = account.check_balance(request.user.username).amount

    
    return render(request , 'account/deposit.html' , {})
