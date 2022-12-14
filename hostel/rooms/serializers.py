from rest_framework import serializers

from dormitory.serializers import DormitorySerializer


class RoomsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    room_number = serializers.IntegerField()
    floor = serializers.IntegerField()
    free_places = serializers.IntegerField()
    dormitory = DormitorySerializer.DormitoryRepresentation(read_only=True)

    class RoomsRepresentation(serializers.RelatedField):
        def to_representation(self, value):
            return f'{value.room_number}'
