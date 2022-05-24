from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role=self.validated_data['role']
        )

        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class CoffeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'


class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
