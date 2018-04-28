from django.db import models

# Create your models here.
class Complements(models.Model):
	complement = models.CharField(max_length=1000)
	def __str__(self):
		return self.complement