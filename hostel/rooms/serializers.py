from rest_framework import serializers

from dormitory.serializers import DormitorySerializer


class RoomsSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    floor = serializers.IntegerField()
    dormitory = DormitorySerializer.DormitoryRepresentation(read_only=True)
