from django.db import models


class PhoneNumber(models.Model):
    number = models.CharField(max_length=11, unique=True)
    operator = models.CharField(max_length=20)
    region = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.number} - {self.operator} - {self.region}"

