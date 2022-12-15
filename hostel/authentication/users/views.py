from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserView(APIView):
    def get(self, request):
        if not request.user.id:
            return Response('unauthorized', 401)
        print(request.headers)
        user = get_object_or_404(CustomUser.objects.all(), pk=request.user.id)
        serializer = CustomUserSerializer(user)
        user_data = serializer.data
        user_data.pop('password', None)
        return Response({
            "user": user_data
        })

    def post(request):
        user_data = request.data
        serializer = CustomUserSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({
            "user": serializer.data
        })

    def put(self, request):
        if not request.user.id:
            return Response('unauthorized', 401)
        saved_user = get_object_or_404(CustomUser.objects.all(), pk=request.user.id)
        serializer = CustomUserSerializer(instance=saved_user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({
                "user": serializer.data
            })
        return Response(f"Invalid data", 501)

    def delete(self, request):
        if not request.user.id:
            return Response('unauthorized', 401)
        user = get_object_or_404(CustomUser.objects.all(), pk=request.user.id)
        user.delete()
        return Response({
            "message": f"User with id '{request.user.id}' has been deleted."
        }, status=204)
