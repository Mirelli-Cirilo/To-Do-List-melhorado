from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(null=True,blank=True)
    completo = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        ordering = ['completo']
