from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework import permissions
from account.models import Account 
from api.serializer import TutorialSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from custom.balance import Balance 
from decimal import *
from statement.models import Statement
import datetime
 

# Create your views here.
 
@api_view(['POST', 'GET', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def modify(request):
    # find tutorial by pk (id)
    
    
    if request.method == 'POST': 
        print(request.user.id)

        try: 
            tutorial = Account.objects.get(account=request.user.username) 
            # check balance 
            account = Balance()
            balance = account.check_balance(request.user.username).amount
            if balance < Decimal(request.POST.get('amount') or balance == 0 ):
                return JsonResponse({'detail': 'nofunds'}, status=status.HTTP_404_NOT_FOUND) 
            else:
                tutorial.amount = tutorial.amount -  Decimal(request.POST.get('amount'))
                tutorial.save()
                
               
                # statement for sender 
                statementdata = {
                   
                    "operation":"Swipe Pay ",
                    "amount":Decimal(request.POST.get('amount')) ,
                    "date":datetime.datetime.now() ,
                    "account":request.user.username ,
                }
                account.statementcreate(statementdata)

                # statement for receiver 
                # statementdata = {
                   
                #     "operation":"Swipe Pay ",
                #     "amount":Decimal(request.POST.get('amount')) ,
                #     "date":datetime.datetime.now() ,
                #     "account":request.POST.get('account'),
                # }
                # account.statementcreate(statementdata)

                tutorial_serializer = TutorialSerializer(tutorial) 
              
                return JsonResponse({'detail': 'success'}, status=status.HTTP_404_NOT_FOUND) 
                # return JsonResponse(tutorial_serializer.data) 
        except Account.DoesNotExist: 
            return JsonResponse({'detail': 'The model does not exist'}, status=status.HTTP_404_NOT_FOUND) 
            