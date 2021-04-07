from rest_framework import serializers
from complex.models import Complex,Block,Unit
from account.models import User
from family.models import Father,Mother,Family
# from smart_objects.models import 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=('password',)