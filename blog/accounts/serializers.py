
from rest_framework import serializers


class UserAuthenticateSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, allow_null=False, allow_blank=False, max_length=100)
    password = serializers.CharField(
        required=True, allow_null=False, allow_blank=False, max_length=128)


class UserTokenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()


class TokenSerializer(serializers.Serializer):
    jwt = serializers.CharField(max_length=242, min_length=242)
    user = UserTokenSerializer()
