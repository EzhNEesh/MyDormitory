from django.db import models
from authentication.users.models import CustomUser


class Dormitory(models.Model):
    address = models.CharField(max_length=100, unique=True)
    floors_count = models.IntegerField()
    rooms_on_floor_count = models.IntegerField()
    places_in_room_count = models.IntegerField()
    university_info = models.CharField(max_length=100)
    busy_places = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
