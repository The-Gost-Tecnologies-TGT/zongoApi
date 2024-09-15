from django.db import models

class Membros(models.Model):
    # Definição das opções de nível de ensino como choices
    ENSINO_CHOICES = [
        ('EM', 'Ensino Médio'),
        ('LC', 'Licenciatura'),
        ('ME', 'Mestrado'),
        ('PG', 'Pós-Graduação'),
        ('DO', 'Doutoramento'),
    ]
    
    # Definição das opções de estado
    ESTADO_CHOICES = [
        ('ESPERA', 'Em Espera'),
        ('ENCAMINHADO', 'Encaminhado'),
    ]

    # Campos do modelo
    nome = models.CharField(max_length=255)
    numero_bi = models.CharField(max_length=22, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    ensino = models.CharField(max_length=2, choices=ENSINO_CHOICES)

    # Estado com valor padrão 'Em Espera'
    estado = models.CharField(max_length=12, choices=ESTADO_CHOICES, default='ESPERA')

    # Campos de documentos (aceitam apenas arquivos PDF)
    bi_identidade = models.FileField(upload_to='documentos/bi/', blank=True, null=True)
    certificado_medio = models.FileField(upload_to='documentos/certificados/medio/', blank=True, null=True)
    certificado_diploma = models.FileField(upload_to='documentos/certificados/diploma/', blank=True, null=True)
    certificado_best = models.FileField(upload_to='documentos/certificados/best/', blank=True, null=True)
    cv = models.FileField(upload_to='documentos/cv/', blank=True, null=True)
    foto_passe = models.ImageField(upload_to='documentos/foto_passe/', blank=True, null=True)
    cedula_maritima = models.FileField(upload_to='documentos/cedula_maritima/', blank=True, null=True)

    # Campo de observações
    obs = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
