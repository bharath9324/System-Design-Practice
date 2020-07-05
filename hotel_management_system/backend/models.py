from django.db import models


class Hotel(models.Model):
	name = models.CharField(max_length=80)
	city = models.CharField(max_length=80)


class Rooms(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	capacity = models.IntegerField()
	price = models.FloatField()

class Visitor(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

class Reservation(models.Model):
	visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
	room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
