from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TransactionForm , TransactionCreate , TransactionAirtime
from deepface import DeepFace
import pandas as pd
import base64
from django.conf import settings
from face.facecall import Facecall
from .models import Transaction
from custom.balance import Balance
from urllib.request import urlopen
from urllib.parse import quote
from custom.balance import Balance 
from django.contrib import messages
import datetime




   
def home_view(request , *args ,**kwargs):  
    # print(static) 
    return render(request , "home.html" , {})

def airtime_transaction(request):
    create_form = TransactionAirtime()
    if request.method == "POST":
        create_form = TransactionAirtime(request.POST)

        if create_form.is_valid():
            # print(create_form.cleaned_data['provider'])
            amount = create_form.cleaned_data['amount']
            provider = create_form.cleaned_data['provider']
            number = str(create_form.cleaned_data['recipient'])
            
            # BulkSMS Webservice username for sending SMS.
            # Get it from User Configuration. Its case sensitive.
            account = Balance()
            balance = account.check_balance(request.user.id).amount
            if balance < amount:
                messages.add_message(request, messages.ERROR, ' insufficient balance')
                return redirect('/transaction/airtime/') 
            else:
                username = "Kidkudzy"

                # Webservices token for above Webservice username
                token = "7e51158d678553beeae996157bb7b087"

                # BulkSMS Webservices URL
                bulksms_ws = "http://portal.bulksmsweb.com/index.php?app=ws"

                # destination numbers, comma seperated or use #groupcode for sending to group
                # destinations = "#devteam,263071077072,26370229338"
                # destinations = "26300123123123,26300456456456"  #for multiple recipients

                destinations = number

                # SMS Message to send
                message = "You have received $"+str(amount)+" "+provider+" airtime \n from  BIPAY SYSTEM"

                # send via BulkSMS HTTP API

                ws_str = bulksms_ws + "&u=" + username + "&h=" + token + "&op=pv"
                ws_str = ws_str + "&to=" + quote(destinations) + "&msg=" + quote(message)


                http_response = urlopen(ws_str).read()

                


                statement = Balance()
        
                statementdata = {
                    "user_id":request.user.id ,
                    "operation":"Airtime",
                    "amount":amount ,
                    "date":datetime.datetime.now() ,
                    "account":number 
                }
                statement.statementcreate(statementdata)
                messages.add_message(request, messages.INFO, ' Airtime Transfer Successful')
    context = {
        'form':create_form
    }

    return render(request , "transactions/airtime.html" , context)



def view_transaction(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions':transactions
    }
    return render(request , "transactions/view.html" , context)


def create_transaction(request):   

    create_form = TransactionCreate()
    if request.method == "POST":
        create_form = TransactionCreate(request.POST)
        

        if create_form.is_valid():
            # print(type(create_form.cleaned_data['amount']))
            # print(request.username)
            data = request.POST.get('imagebase64').partition(",")[2]
           
            # call to authentication class 
            facecall = Facecall()
            if(facecall.face_authenticate(data)):
                create_form.cleaned_data['user_id'] = 1

                # check available abalnce 
                account = Balance()
                amount = account.check_balance(request.user.id).amount
                if amount < create_form.cleaned_data['amount']:
                    messages.add_message(request, messages.ERROR, ' insufficient balance')
                    return redirect('/transaction/create/') 
                else:
                    
                    account.transferout(user_id = request.user.id , amount = create_form.cleaned_data['amount'])
                    # record statement
                    statement = Balance()
      
                    statementdata = {
                        "user_id":request.user.id ,
                        "operation":"transfer",
                        "amount":request.POST.get('amount') ,
                        "date":datetime.datetime.now() ,
                        "account":request.POST.get('account') 
                    }
                    statement.statementcreate(statementdata)

                    messages.add_message(request, messages.INFO, ' transfer successful')
                    return redirect('/transaction/create/') 
    
                    

                Transaction.objects.create(**create_form.cleaned_data)
                create_form = TransactionCreate()
                
            else:
                print("authentication failure")
        
    context = {
        'form':create_form
    }
    return render(request , "transactions/create.html" , context)
