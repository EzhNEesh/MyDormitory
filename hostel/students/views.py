from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404

from .models import Students
from .serializers import StudentsSerializer
from dormitory.models import Dormitory
from rooms.models import Rooms
from rooms.serializers import RoomsSerializer
from settlers.models import Settlers
from settlers.serializers import SettlersSerializer


class StudentsView(APIView):
    def get(self, request, dormitory_pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        students = Students.objects.all().filter(dormitory=dormitory.id)
        serializer = StudentsSerializer(students, many=True)
        return Response({"students": serializer.data})

    def post(self, request, dormitory_pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = Dormitory.objects.get(id=dormitory_pk, user=request.user.id)
        if not dormitory:
            return Response("Not found", 404)

        settler_id = request.data.get('settler_id')
        settler = get_object_or_404(Settlers, pk=settler_id)
        student_data = SettlersSerializer(settler).data
        print(student_data == dormitory.id)
        if not student_data or int(student_data['dormitory']) != dormitory.id:
            return Response('Not found', 404)
        student_data['dormitory'] = dormitory

        room_id = request.data.get('room_id')
        room = get_object_or_404(Rooms, pk=room_id)
        if int(room.free_places) == 0:
            return Response({
                "response": "the room is full"
            }, status=500)
        room.free_places -= 1
        room.save()
        student_data['room'] = room

        student = Students.objects.create(**student_data)
        if not student:
            return Response("Invalid data", 500)
        settler.delete()
        serializer = StudentsSerializer(student)
        return Response({
            "student": serializer.data
        })

class StudentsPkView(APIView):
    def get(self, request, dormitory_pk, pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        student = get_object_or_404(Students, pk=pk)
        serializer = StudentsSerializer(student)
        room_id = serializer.data['room']
        room = Rooms.objects.get(id=room_id)
        if not room or dormitory.id != room.dormitory.id:
            return Response("Unauthorized", 401)
        return Response({"student": serializer.data})

    def delete(self, request, dormitory_pk, pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        student = get_object_or_404(Students, pk=pk)
        serializer = StudentsSerializer(student)
        room_id = serializer.data['room']
        room = Rooms.objects.get(id=room_id)
        if not room or dormitory.id != room.dormitory.id:
            return Response("Unauthorized", 401)
        student.delete()
        return Response({
            "message": f"Student with id '{pk}' has been deleted."
        }, status=204)
