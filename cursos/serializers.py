from django.db.models import fields
from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        #Adicionando configuração que o email não vai ser apresentado quando consultado. Apenas será mostrado na hora do cadastro de uma avaliação
        extra_kwargs = {
            'email': {'write_only': True}
        }
        
        model = Avaliacao
        #Campos que serão apresentado quando solicitado pelo Cliente
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'nota',
            'criacao',
            'ativo'
        )
       
        
class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship, é preferivel que seja usado em relacionamentos 1 para 1
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    #HyperLinked Related Field
    
  #  avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
  
    #Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )