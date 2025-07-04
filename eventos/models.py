from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
