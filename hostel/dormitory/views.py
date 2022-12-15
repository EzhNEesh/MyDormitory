#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404
from django.db.utils import IntegrityError

from .models import Dormitory
from .serializers import DormitorySerializer
from rooms.views import RoomsManager


class DormitoryView(APIView):

    def get(self, request):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitories = Dormitory.objects.all().filter(user=str(request.user.id))
        if not dormitories:
            return Response('Dormitories not found or access denied', 404)
        serializer = DormitorySerializer(dormitories, many=True)
        return Response({
            "dormitories": serializer.data
        })

    def post(self, request):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory_data = request.data
        dormitory_data['user'] = request.user
        try:
            dormitory_data['busy_places'] = 0
        except KeyError:
            return Response('Invalid data', 400)
        try:
            dormitory = Dormitory.objects.create(**dormitory_data)
        except IntegrityError:
            return Response('Dormitory address must be unique', 501)
        serializer = DormitorySerializer(dormitory)

        try:
            rooms_data = {
                'rooms_on_floor_count': int(dormitory_data['rooms_on_floor_count']),
                'floors_count': int(dormitory_data['floors_count']),
                'places_in_room_count': int(dormitory_data['places_in_room_count']),
                'dormitory': dormitory
            }
        except KeyError:
            return Response('Invalid data', 400)
        rooms_manager = RoomsManager()
        rooms_manager.create_rooms(rooms_data)
        return Response({
            "dormitory": serializer.data
        }, 201)


class DormitoryPkView(APIView):
    def get(self, request, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = get_object_or_404(Dormitory.objects.all(), pk=pk, user=request.user.id)
        serializer = DormitorySerializer(dormitory)
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
        return Response(f"Invalid data", 501)

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
