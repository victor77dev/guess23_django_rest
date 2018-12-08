# users.serializers
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', )

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', )
