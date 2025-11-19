from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        write_only_fields = ('password')
        read_only_fields = ('data_cadastro')
    