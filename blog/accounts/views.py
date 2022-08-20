
from django.contrib.auth import authenticate, login

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts import serializers

from blog.utils.error_response import ErrorResponse


class LoginView(viewsets.ViewSet):

    permission_classes = [AllowAny]

    @action(['post'], detail=True)
    def login(self, request):

        serializer = serializers.UserAuthenticateSerializer(
            data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(
                "Campos incorretos", status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(request, **serializer.data)

        if user is None:
            return ErrorResponse(
                "Usuário e/ou senha incorreto(s)", status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)
        token = RefreshToken.for_user(user)

        serializer = serializers.TokenSerializer(
            {"jwt": token.access_token, "user": user})

        return Response(serializer.data, status=status.HTTP_201_CREATED)
