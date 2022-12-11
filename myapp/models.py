from django.db import models

class Portafolio(models.Model):
    foto = models.URLField(max_length=200)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tags = models.CharField(max_length=200)
    urlgithub = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo + " - " + str(self.tags)

    class Meta:
        db_table = "myapp_portafolio"

class Visitas(models.Model):
    ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)