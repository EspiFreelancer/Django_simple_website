from django.db import models

# Create your models here.

class Networks(models.Model):
	name = models.CharField(max_length=255, verbose_name="Nombre Red")
	url = models.URLField(max_length=255, null=True, blank=True, verbose_name="Url enlace")
	key = models.SlugField(max_length=100, unique=True, help_text ="Ejemplo: TWITTER_LINK",
		verbose_name="Palabra clave de Red")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "red"
		verbose_name_plural = "redes"
		ordering = ['name']

	def __str__(self):
		return self.name