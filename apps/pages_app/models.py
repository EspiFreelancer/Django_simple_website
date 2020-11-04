from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Generic_page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"

    def __str__(self):
        return self.title
    