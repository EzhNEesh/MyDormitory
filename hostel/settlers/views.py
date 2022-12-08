from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.generics import get_object_or_404

from .models import Settlers
from .serializers import SettlersSerializer
from dormitory.models import Dormitory


class SettlersView(APIView):

    def get(self, request, dormitory_pk, pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        settler = Settlers.objects.get(
            id=pk,
            dormitory=dormitory
        )
        if not settler:
            return Response("Not found", 404)
        serializer = SettlersSerializer(settler)
        return Response({"rooms": serializer.data})

    def post(self, request, dormitory_pk):
        if not request.user.id:
            return Response('unauthorized', 401)
        settler_data = request.data
        dormitory = Dormitory.objects.get(id=dormitory_pk, user=request.user.id)
        if not dormitory:
            return Response("Not found", 404)
        settler_data['dormitory'] = dormitory
        settler = Settlers.objects.create(**settler_data)
        if not settler:
            return Response("Invalid data", 500)
        serializer = SettlersSerializer(settler)
        return Response({
            "settler": serializer.data
        })

    def delete(self, request, dormitory_pk, pk):
        dormitory = Dormitory.objects.get(
            id=dormitory_pk,
            user=request.user
        )
        if not dormitory:
            return Response("Unauthorized", 401)
        settler = Settlers.objects.get(
            id=pk,
            dormitory=dormitory
        )
        if not settler:
            return Response("Not found", 404)
        settler = get_object_or_404(Settlers.objects.all(), pk=pk)
        settler.delete()
        return Response({
            "message": f"Settler with id '{pk}' has been deleted."
        }, status=204)
