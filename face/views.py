from django.shortcuts import render
from django.http import HttpResponse
# from .forms import TransactionForm
from deepface import DeepFace
import pandas as pd
import base64
from django.conf import settings





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

    context = {}
    return render(request , "face/register.html" , context)
def login(request):

    context = {}
    return render(request , "face/login.html" , context)
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
            

        df = DeepFace.find(img_path = settings.MEDIA_ROOT+'temp.jpg', db_path = settings.MEDIA_ROOT+'sets')

        if df.shape[0] > 0 :
            matched  = df.iloc[0].identity
            print(matched)
        else:
            print("no match")

        # print(request.POST.get('account')+"test")
    context = {}
    return render(request , "face/face.html" , context)

    

    

    