from rest_framework import serializers

from rooms.serializers import RoomsSerializer


class StudentsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    fullname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    phone = serializers.CharField(max_length=50)
    flg = serializers.BooleanField()
    room = RoomsSerializer.RoomsRepresentation(read_only=True)
