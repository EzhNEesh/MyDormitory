from django.db import models
from django.utils.translation import ugettext_lazy as _
from dormitory.models import Dormitory


class Settlers(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=50)
    flg = models.BooleanField(default=False)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
