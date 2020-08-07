from django.shortcuts import render
from django.http import HttpResponse
from .forms import TransactionForm , TransactionCreate , TransactionAirtime
from deepface import DeepFace
import pandas as pd
import base64
from django.conf import settings
from face.facecall import Facecall
from .models import Transaction
from urllib.request import urlopen
from urllib.parse import quote



   
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

            print(http_response)
    context = {
        'form':create_form
    }

    return render(request , "transactions/airtime.html" , context)

def statement_transaction(request):
    # transactions = Transaction.objects.all()
    context = {
        # 'transactions':transactions
    }
    return render(request , "transactions/statement.html" , context)

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
            # print(request.username)
            data = request.POST.get('imagebase64').partition(",")[2]
           
            # call to authentication class 
            facecall = Facecall()
            if(facecall.face_authenticate(data)):
                create_form.cleaned_data['user_id'] = 1
                Transaction.objects.create(**create_form.cleaned_data)
                create_form = TransactionCreate()
                
            else:
                print("authentication failure")
        
    context = {
        'form':create_form
    }
    return render(request , "transactions/create.html" , context)
