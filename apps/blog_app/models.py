from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")
    slug = models.SlugField(max_length=50, unique=True, blank=True,
        help_text = "Opcional. Nombre de articulo mostrado en la barra de navegación.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "artículo"
        verbose_name_plural = "artículos"
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)