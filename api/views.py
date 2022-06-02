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
@api_view(['POST'])
def addCoffee(request):
    serializer = CoffeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
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


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getSingleItem(request, pk):
    coffee = Coffee.objects.get(id=pk)
    serializer = CoffeeSerializers(coffee, many=False)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def updateCoffee(request, pk):
    coffee = Coffee.objects.get(id=pk)
    serializer = CoffeeSerializers(coffee, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def addRecommendedCoffee(request):
    serializer = RecommendedCoffeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
    else:
        data = serializer.errors
    return Response(data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getRecommendedCoffee(request):
    coffee = RecommendedCoffee.objects.all()
    serializer = RecommendedCoffeeSerializers(coffee, many=True)
    return Response(
        {
            "total_items": RecommendedCoffee.objects.count(),
            "coffee": serializer.data
        }
    )


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getSingleRecommendedItem(request, pk):
    coffee = RecommendedCoffee.objects.get(id=pk)
    serializer = RecommendedCoffeeSerializers(coffee, many=False)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def updateRecommendedCoffee(request, pk):
    coffee = RecommendedCoffee.objects.get(id=pk)
    serializer = RecommendedCoffeeSerializers(coffee, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getRole(request, pk):
    token = Token.objects.get(key=pk)
    serializer = TokenSerializers(token, many=False)
    user = serializer.data['user']
    account = Account.objects.get(username=user)
    accountSerializer = RegistrationSerializer(account, many=False)

    return Response(
        {
            "role": accountSerializer.data['role'],
            "user": user
        }
    )


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def isFavourite(request):
    serializer = IsFavouriteSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
    else:
        data = serializer.errors
    return Response(data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getFavourite(request):
    coffee = IsFavourite.objects.filter(user=request.user)
    serializer = IsFavouriteSerializers(coffee, many=True)
    return Response({
        "total_favourite": coffee.count(),
        "favourite": serializer.data
    })


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def makeOrder(request):
    serializer = OrderSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
    else:
        data = serializer.errors
    return Response(data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getOrder(request):
    order = Order.objects.all()
    serializer = OrderSerializers(order, many=True)
    return Response(
        {
            "all_orders": serializer.data
        }
    )


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response({'response': 'order was deleted!'})
