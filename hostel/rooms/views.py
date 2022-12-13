from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404

from .models import Rooms
from .serializers import RoomsSerializer
from dormitory.models import Dormitory


class RoomsManager():

    def create_rooms(self, data):
        rank = 1
        buf = data['rooms_on_floor_count']
        while buf:
            rank *= 10
            buf //= 10
        for floor in range(1, data['floors_count'] + 1):
            for room in range(1, data['rooms_on_floor_count'] + 1):
                Rooms.objects.create(
                    id=floor * rank + room,
                    floor=floor,
                    dormitory=data['dormitory'],
                    free_places=int(data['places_in_room_count'])
                )

class RoomsView(APIView):

    def get(self, request, dormitory_pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        rooms = Rooms.objects.all().filter(dormitory=dormitory_pk)
        serializer = RoomsSerializer(rooms, many=True)
        return Response({"rooms": serializer.data})

class RoomsPkView(APIView):

    def get(self, request, dormitory_pk, pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        room = get_object_or_404(Rooms, pk=pk)
        serializer = RoomsSerializer(room)
        return Response({"room": serializer.data})
