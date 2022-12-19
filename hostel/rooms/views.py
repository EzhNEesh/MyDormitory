from rest_framework.views import APIView
from rest_framework.views import Response
from django.db.utils import IntegrityError

from .models import Rooms
from .serializers import RoomsSerializer
from dormitory.models import Dormitory


class RoomsManager:
    @staticmethod
    def create_rooms(data):
        try:
            rank = 1
            buf = data['rooms_on_floor_count']
            while buf:
                rank *= 10
                buf //= 10
            for floor in range(1, data['floors_count'] + 1):
                for room in range(1, data['rooms_on_floor_count'] + 1):
                    Rooms.objects.create(
                        room_number=floor * rank + room,
                        floor=floor,
                        dormitory=data['dormitory'],
                        free_places=int(data['places_in_room_count']),
                        places=int(data['places_in_room_count'])
                    )
        except TypeError:
            raise TypeError
        except IntegrityError:
            raise IntegrityError


class RoomsView(APIView):
    def post(self, request, dormitory_pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Dormitory not found or access denied", 404)
        partition, page = min(int(request.data.get('partition', 6)), 25), int(request.data.get('page', 1))
        rooms = Rooms.objects.all().filter(dormitory=dormitory_pk)[(page - 1) * partition:page * partition]
        serializer = RoomsSerializer(rooms, many=True)
        return Response({"rooms": serializer.data})


class RoomsPkView(APIView):
    def get(self, request, dormitory_pk, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Dormitory not found or access denied", 404)
        room = Rooms.objects.get(
            room_number=pk,
            dormitory=dormitory
        )
        serializer = RoomsSerializer(room)
        return Response({"room": serializer.data})
