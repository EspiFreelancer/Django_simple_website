from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=50)
	image = models.ImageField(upload_to='blog', null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "artículo"
		verbose_name_plural = "artículos"		