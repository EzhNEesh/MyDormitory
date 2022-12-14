from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404
from django.db.utils import IntegrityError

from .models import Settlers
from .serializers import SettlersSerializer
from dormitory.models import Dormitory


class SettlersView(APIView):
    def get(self, request, dormitory_pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Dormitory not found or access denied", 404)
        settlers = Settlers.objects.all().filter(dormitory=dormitory)
        if not settlers:
            return Response("Settlers not found", 404)
        serializer = SettlersSerializer(settlers, many=True)
        return Response({"settlers": serializer.data})

    def post(self, request, dormitory_pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        settler_data = request.data
        dormitory = Dormitory.objects.get(id=dormitory_pk, user=request.user.id)
        if not dormitory:
            return Response("Dormitory not found or access denied", 404)
        settler_data['dormitory'] = dormitory
        settler = None
        try:
            settler = Settlers.objects.create(**settler_data)
        except IntegrityError:
            return Response("Email must be Unique", 501)
        if not settler:
            return Response("Invalid data", 501)
        serializer = SettlersSerializer(settler)
        return Response({
            "settler": serializer.data
        })

class SettlersPkView(APIView):
    def get(self, request, dormitory_pk, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Dormitory not found or access denied", 404)
        settler = Settlers.objects.get(
            id=pk,
            dormitory=dormitory
        )
        if not settler:
            return Response("Settler not found", 404)
        serializer = SettlersSerializer(settler)
        return Response({"settler": serializer.data})

    def delete(self, request, dormitory_pk, pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Dormitory not found or access denied", 404)
        settler = Settlers.objects.get(
            id=pk,
            dormitory=dormitory
        )
        if not settler:
            return Response("Settler not found", 404)
        settler.delete()
        return Response({
            "message": f"Settler with id '{pk}' has been deleted."
        }, status=204)
