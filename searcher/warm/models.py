from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(max_length=50)
    price = models.IntegerField()
    meters = models.IntegerField()

    def __str__(self):
        return self.address


class Coordinates(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address.__str__()


class District(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    district = models.TextField(max_length=100)

    def __str__(self):
        return self.district


class Histogram(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    histogram_price_district = models.ImageField()
    histogram_meters_district = models.ImageField()


class CoordinateCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.city.__str__()
