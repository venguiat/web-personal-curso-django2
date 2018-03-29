from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=90, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    # Fecha de creacion
    # auto now add se ejecuta solo la primera vez
    created = models.DateTimeField(auto_now_add=True)
    # Fecha de ultima modificacion
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
    def __str__(self):
        return self.title