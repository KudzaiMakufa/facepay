from django.shortcuts import render
from .models import Statement
from rest_framework import viewsets
from rest_framework import permissions
from custom.serializer import UserSerializer
from django.http import HttpResponse
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Statement.objects.all()
    serializer_class = UserSerializer
    print(serializer_class)
    permission_classes = [permissions.IsAuthenticated]



def view_statement(request):
    statement = None 
   
    try:
        statement = Statement.objects.filter(account = request.user.username)
    except :
        pass
    context = {
        'statements':statement
    }
    return render(request , "statement/statement.html" , context)
def testapi():
    pass