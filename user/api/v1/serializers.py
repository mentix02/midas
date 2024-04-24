from rest_framework import serializers

from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, validated_data) -> User:
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')
