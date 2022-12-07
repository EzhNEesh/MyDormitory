#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser.objects.all(), pk=pk)
        serializer = CustomUserSerializer(user)
        return Response({
            "user": serializer.data
        })

    def post(self, request):
        user_data = request.data
        serializer = CustomUserSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({
            "user": serializer.data
        })

    def put(self, request, pk):
        saved_user = get_object_or_404(CustomUser.objects.all(), pk=pk)
        serializer = CustomUserSerializer(instance=saved_user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({
            "user": serializer.data
        })

    def delete(self, request, pk):
        user = get_object_or_404(CustomUser.objects.all(), pk=pk)
        user.delete()
        return Response({
            "message": f"User with id '{pk}' has been deleted."
        }, status=204)
