from rest_framework import status
from rest_framework.views import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.views import APIView
from django.db.utils import IntegrityError

from .users.serializers import CustomUserSerializer
from .users.models import CustomUser
from .serializers import MyTokenObtainPairSerializer


class AuthView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        email = request.data.get('email')
        user = CustomUser.objects.filter(email=email)[0]
        user_serializer = CustomUserSerializer(user)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user_data = user_serializer.data
        user_data.pop('password', None)
        return Response({
            "jwt": serializer.validated_data,
            "user": user_data
        }, status=status.HTTP_200_OK)


class RegisterView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        user_data = request.data
        user_serializer = CustomUserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            try:
                user_saved = user_serializer.save()
            except IntegrityError:
                return Response("Field email must be unique", 501)

        serializer = self.get_serializer(data=user_data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user_response = user_serializer.data
        user_response.pop('password', None)

        return Response({
            "jwt": serializer.validated_data,
            "user": user_response
        }, status=status.HTTP_200_OK)
