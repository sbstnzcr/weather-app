from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

class Weather(models.Model):
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    temperature = models.FloatField()
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
