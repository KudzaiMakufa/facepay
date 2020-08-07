from django.shortcuts import render
from django.http import HttpResponse
from .forms import TransactionForm , TransactionCreate
from deepface import DeepFace
import pandas as pd
import base64
from django.conf import settings
from face.facecall import Facecall
from .models import Transaction



   
def home_view(request , *args ,**kwargs):  
    # print(static) 
    return render(request , "home.html" , {})


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
