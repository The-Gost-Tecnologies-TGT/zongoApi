from rest_framework import serializers
from .models import Membros

class MembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membros
        fields = [
            'id', 
            'nome', 
            'numero_bi', 
            'telefone', 
            'email', 
            'ensino', 
            'estado',
            'bi_identidade', 
            'certificado_medio', 
            'certificado_diploma', 
            'certificado_best', 
            'cv', 
            'foto_passe', 
            'cedula_maritima', 
            'obs'
        ]
        # Os campos de arquivos podem ser marcados como read-only, dependendo do uso
        extra_kwargs = {
            'bi_identidade': {'required': False, 'allow_null': True},
            'certificado_medio': {'required': False, 'allow_null': True},
            'certificado_diploma': {'required': False, 'allow_null': True},
            'certificado_best': {'required': False, 'allow_null': True},
            'cv': {'required': False, 'allow_null': True},
            'foto_passe': {'required': False, 'allow_null': True},
            'cedula_maritima': {'required': False, 'allow_null': True},
            'obs': {'required': False, 'allow_blank': True}
        }
