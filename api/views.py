from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *

from rest_framework.authtoken.models import Token


# Create your views here.

class RegistrationView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully register a new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['role'] = account.role
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getCoffee(request):
    coffee = Coffee.objects.all()
    serializer = CoffeeSerializers(coffee, many=True)
    return Response(
        {
            "total_items": Coffee.objects.count(),
            "coffee": serializer.data
        }
    )

@api_view(['GET'])
def getRole(request, pk):
    token = Token.objects.get(key=pk)
    serializer = TokenSerializers(token, many=False)
    user = serializer.data['user']
    account = Account.objects.get(username=user)
    accountSerializer = RegistrationSerializer(account, many=False)

    return Response(accountSerializer.data['role'])