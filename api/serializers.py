from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'email', 'username', 'password', 'role', 'profile', 'contact', 'address', 'shopName']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            name=self.validated_data['name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role=self.validated_data['role'],
            profile=self.validated_data['profile'],
            contact=self.validated_data['contact'],
            address=self.validated_data['address'],
            shopName=self.validated_data['shopName']
        )

        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class CoffeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'


class RecommendedCoffeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecommendedCoffee
        fields = '__all__'


class IsFavouriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = IsFavourite
        fields = '__all__'

    def validate(self, data):
        if data['coffee']:
            # print('test')
            # for n in IsFavourite.objects.all():
            #     print(n)
            #     if n.coffee == data['coffee']:
            #         raise serializers.ValidationError({
            #             "Error": "This item already in your favourite list"
            #         })

            return data


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
