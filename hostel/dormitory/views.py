#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404

from .models import Dormitory
# from authentication.users.models import CustomUser
from .serializers import DormitorySerializer


class DormitoryView(APIView):
    def get(self, request, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = get_object_or_404(Dormitory.objects.all(), pk=pk, user=str(request.user.id))
        serializer = DormitorySerializer(dormitory)
        return Response({
            "dormitory": serializer.data
        })

    def get(self, request):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitories = Dormitory.objects.all().filter(user=str(request.user.id))
        serializer = DormitorySerializer(dormitories, many=True)
        return Response({
            "dormitories": serializer.data
        })

    def post(self, request):
        dormitory_data = request.data
        dormitory_data['user'] = request.user
        dormitory = Dormitory.objects.create(**dormitory_data)
        serializer = DormitorySerializer(dormitory)
        #return Response('meow')
        return Response({
            "dormitory": serializer.data
        })

    def put(self, request, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        saved_dormitory = get_object_or_404(Dormitory.objects.all(), pk=pk, user=request.user.id)
        serializer = DormitorySerializer(instance=saved_dormitory, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            dormitory_saved = serializer.save()
            return Response({
                "dormitory": serializer.data
            })
        return Response({
            f"Dormitory with id '{pk}' does not exist"
        })

    def delete(self, request, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = get_object_or_404(Dormitory.objects.all(), pk=pk, user=str(request.user.id))
        if dormitory:
            dormitory.delete()
            return Response({
                "message": f"Dormitory with id '{pk}' has been deleted."
            }, status=204)
        return Response({
            f"Dormitory with id '{pk}' does not exist"
        })
