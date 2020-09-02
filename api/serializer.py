from rest_framework import serializers 
from account.models import Account
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Account
        fields = ('user_id',
                  'amount',
                 )