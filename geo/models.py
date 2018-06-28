from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.


class Fish(models.Model):
	title = models.CharField(max_length=50)
	#pounds = models.ManyToManyField(Pound)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class Pound(models.Model):
	title = models.CharField(max_length=50)
	fishes = models.ManyToManyField(Fish)
	position = GeopositionField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)

