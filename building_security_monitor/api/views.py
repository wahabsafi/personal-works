from complex.models import Complex,Block,Unit
from account.models import User
from family.models import Father,Mother,Family
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer
# Create your views here.
class UserList(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
