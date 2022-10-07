from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Games(models.Model):
	"""
	Model which stores all data about the games
	which will be displayed on the website
	"""
	choices =(
		('FPS','FPS'),
		('MOBA','MOBA'),
		('ADVANTURE','ADVANTURE'),
		('COOP','COOP'),
		('PVP','PVP'),
	)
	name = models.CharField(max_length=200, null=True, blank=True)
	short_content = models.CharField(max_length=200, null=True, blank=True)
	contetnt= models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	version = models.DecimalField(decimal_places=3, max_digits=100, null=True, blank=True)
	author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
	category = models.CharField(max_length=200, choices=choices, )

	# class Met
	def __str__(self) -> str:
		return self.name