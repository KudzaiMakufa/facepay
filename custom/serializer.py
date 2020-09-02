from statement.models import Statement
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statement
        fields = [ 'user_id', 'operation', 'amount', 'date' ,'account']