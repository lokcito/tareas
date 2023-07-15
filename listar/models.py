from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 256)
    options = [
        ["Critico", "Critico"], 
        ["Medio", "Medio"],
        ["Bajo", "Bajo"],
        ["Opcional", "Opcional"]
    ]
    tags = models.CharField(max_length = 32, choices = options, default="Opcional")

    class Meta:
        permissions = [("revocar_tarea", "Recover esta tarea")]
        verbose_name_plural = "Administrar Tareas"
    
    def __str__(self):
        return self.title