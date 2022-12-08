from django.db import models
from django.utils.translation import ugettext_lazy as _
from rooms.models import Rooms


class Students(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=50)
    flg = models.BooleanField(default=False)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
