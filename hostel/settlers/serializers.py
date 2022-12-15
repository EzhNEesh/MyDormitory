from rest_framework import serializers

from dormitory.serializers import DormitorySerializer


class SettlersSerializer(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    fullname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    phone = serializers.CharField(max_length=50)
    flg = serializers.BooleanField()
    # dormitory = DormitorySerializer.DormitoryRepresentation(read_only=True)
