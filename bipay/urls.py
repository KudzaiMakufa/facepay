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
from django.urls import path, include 
from transactions.views import home_view , create_transaction , view_transaction , airtime_transaction
from face.views import home_face ,  register ,userlogin , userlogout
from account.views import balance
from statement import views
# REST API 
from rest_framework import routers
from django.conf.urls import url

# this is where url for application rest us added 
router = routers.DefaultRouter()
router.register(r'statement', views.UserViewSet)#eg views.ViewDAta etc 


urlpatterns = [
    #face
    path('', userlogin ,name='login'),
    path('rest/', include(router.urls)),
    path('face/', home_face , name='face'),
    path('register/', register ,name='face'),
    path('login/', userlogin ,name='face'),
    path('face/logout/', userlogout ,name='face'),
    #transactions
    path('transaction/create/', create_transaction),
    path('transaction/view/', view_transaction),
    path('transaction/airtime/', airtime_transaction),
    #admin
    path('admin/', admin.site.urls),
    #account
    path('account/balance/', balance ,name='account'),
    # statement
    path('statement/view/', views.view_statement ,name='statement'),

    # REST API 
    path('apiauth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'apiauth/', include('rest_framework.urls'),namespace='rest_framework'))

    # test two api   
    url(r'^', include('api.urls')),
    

   
    
]
