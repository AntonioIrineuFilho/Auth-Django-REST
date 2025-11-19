from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    PERFIL = [
        ('G', 'GERENTE'),
        ('M', 'MECANICO'),
        ('C', 'CLIENTE')
    ]
    email = models.EmailField(unique=True, blank=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False)
    telefone = models.CharField(max_length=11)
    tipo_perfil = models.CharField(max_length=8, choices=PERFIL)
    data_cadastro = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)
