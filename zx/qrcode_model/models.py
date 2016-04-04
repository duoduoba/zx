from django.db import models


# Create your models here.
class QRData(models.Model):
    redirect = models.CharField(max_length=300)
    count = models.PositiveIntegerField(default=0)
