from rest_framework import status
from rest_framework.views import Response
#from ..users.models import CustomUser
#from rest_framework.views import APIView
#from rest_framework.authentication import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.generics import get_object_or_404

from .users.serializers import CustomUserSerializer
from .users.models import CustomUser
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        email = request.data.get('email')
        #print(CustomUser.objects.filter(email=email))
        user = CustomUser.objects.filter(email=email)[0]
        user_serializer = CustomUserSerializer(user)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response({"jwt": serializer.validated_data, "user": user_serializer.data}, status=status.HTTP_200_OK)