from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email = serializers.EmailField(max_length=50)
    fullname = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50, required=False)
    phone = serializers.CharField(max_length=50)
    # imageUrl = serializers.CharField(null=True)
    # user_id = serializers.PositiveBigIntegerField(unique=True)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        new_password = validated_data.get('password', None)
        if new_password is not None:
            instance.set_password(new_password)
        instance.phone = validated_data.get('phone', instance.phone)

        instance.save()
        return instance

    class UserRepresentation(serializers.RelatedField):
        def to_representation(self, value):
            return f'{value.id}'
