from django.db import models
from ckeditor.fields import RichTextField

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='autos', null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"