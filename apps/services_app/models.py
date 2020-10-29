from django.db import models

# Create your models here.

class Services(models.Model):
	title = models.CharField(max_length=50, verbose_name="Título")
	content = models.CharField(max_length=150, verbose_name="Descripción")
	image = models.ImageField(upload_to='services', verbose_name="Imagen")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "servicio"
		verbose_name_plural = "servicios"
		ordering = ['-created']