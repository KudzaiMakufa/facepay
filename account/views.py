from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def balance(request):



    context = {

    }

    return render(request , 'account/balance.html' , context)
