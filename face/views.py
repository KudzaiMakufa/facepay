from django.shortcuts import render , redirect
from django.http import HttpResponse
# from .forms import TransactionForm
from deepface import DeepFace
import pandas as pd
import base64
from django.conf import settings
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import Account





def face_authenticate(imageBase):  
        # take image as base64 arg
        data = imageBase

        facematch =  False
        imgdata = base64.b64decode(data)
        filename = "{}temp.jpg".format(settings.MEDIA_ROOT)
        
        with open(filename, 'wb') as f:
            f.write(imgdata)
            
        # compare and a
        df = DeepFace.find(img_path = settings.MEDIA_ROOT+'temp.jpg', db_path = settings.MEDIA_ROOT+'sets')

        if df.shape[0] > 0 :
            matched  = df.iloc[0].identity
            
            facematch = True
        else:
            facematch = False
        
        return facematch
def register(request):
    if request.method == "POST":
        data = request.POST.get('imagebase64').partition(",")[2]
    
        if request.POST.get('password') != request.POST.get('password1'):
            messages.add_message(request, messages.ERROR, ' passwords did not match')
            return redirect('/login/')
        else :
            
            if User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password')) and saveImage(data,request.POST.get('username')):
                user = authenticate(request , username=request.POST.get('username'),password = request.POST.get('password'))
                
               
                if user is not None:
               
                     # create account 
                    account = Account(account = request.POST.get('username') , amount = 0 )
                    account.save() 
                    
                else:
                    print("failed to save ")
                    pass

                
                
                


                messages.add_message(request, messages.INFO, ' account created') 
                
                # save images to sets directory 
                return redirect('/login/')
            else :
                messages.add_message(request, messages.ERROR, ' Failed to create account')
                return redirect('/login/')

    context = {}
    return render(request , "face/register.html" , context)
def userlogout(request):
    logout(request)
    return redirect('/login/')
def userlogin(request):
    if request.method == "POST":
   

        
        user = authenticate(username=request.POST.get('email'),password = request.POST.get('password'))
       
        print(user)
        data = request.POST.get('imagebase64').partition(",")[2]
        
           
            # call to authentication class 
        
        if user is not None and face_authenticate(data):
            login(request , user)
            return redirect('/transaction/view/')
        # A backend authenticated the credentials
        else:
        # No backend authenticated the credentials
            messages.add_message(request, messages.ERROR, 'invalid email or password')

    context = {}
    return render(request , "face/login.html" , context)
def saveImage(imageBase,name):
    data = imageBase

    saved  =  False
    imgdata = base64.b64decode(data)
    filename = name+".jpg".format(settings.MEDIA_ROOT+"sets/")
    # filename = name+".jpg".format(settings.MEDIA_ROOT+"sets/")
    
    with open(filename, 'wb') as f:
        if(f.write(imgdata)) :
            saved = True
    return saved 
def home_face(request):  
    # print(static) 
    if request.method == "POST":
        # print(request.POST.get('submit', ''))
        print(request.user)

        data = request.POST.get('account').partition(",")[2]
        imgdata = base64.b64decode(data)
        filename = "{}temp.jpg".format(settings.MEDIA_ROOT)
        # filename = 'promise.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
            

        df = DeepFace.find(img_path = settings.MEDIA_ROOT+'img1.jpg', db_path = settings.MEDIA_ROOT+'sets')

        if df.shape[0] > 0 :
            matched  = df.iloc[0].identity
            print(matched)
        else:
            print("no match")

        # print(request.POST.get('account')+"test")
    context = {}
    return render(request , "face/face.html" , context)

    

    

    