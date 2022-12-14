from django.db import models
from dormitory.models import Dormitory


class Rooms(models.Model):
    room_number = models.PositiveIntegerField()
    floor = models.IntegerField()
    free_places = models.IntegerField(default=3)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
