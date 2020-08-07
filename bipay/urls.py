"""bipay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from transactions.views import home_view , create_transaction , view_transaction 
from face.views import home_face ,  register ,login
from account.views import balance

urlpatterns = [
    #face
    path('', home_view ,name='home'),
    path('face/', home_face ,name='face'),
    path('register/', register ,name='face'),
    path('login/', login ,name='face'),
    #transactions
    path('transaction/create/', create_transaction),
    path('transaction/view/', view_transaction),
    #admin
    path('admin/', admin.site.urls),
    #account
    path('account/balance', balance ,name='account'),

   
    
]
