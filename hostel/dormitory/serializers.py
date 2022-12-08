from rest_framework import serializers

from authentication.users.serializers import CustomUserSerializer


class DormitorySerializer(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    address = serializers.CharField(max_length=100)
    floors_count = serializers.IntegerField()
    rooms_on_floor_count = serializers.IntegerField()
    places_in_room_count = serializers.IntegerField()
    university_info = serializers.CharField(max_length=100)
    user = CustomUserSerializer.UserRepresentation(read_only=True)
    """ class Meta():
        model = Dormitory
        fields = ['id', 'address', 'floors_count', 'rooms_on_floor_count', 'places_in_room_count', 'university_info', 'user']"""

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.floors_count = validated_data.get('floors_count', instance.floors_count)
        instance.rooms_on_floor_count = validated_data.get('rooms_on_floor_count', instance.rooms_on_floor_count)
        instance.places_in_room_count = validated_data.get('places_in_room_count', instance.places_in_room_count)
        instance.university_info = validated_data.get('university_info', instance.university_info)

        instance.save()
        return instance

    class DormitoryRepresentation(serializers.RelatedField):
        def to_representation(self, value):
            return f'{value.id}'
