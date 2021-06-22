import re
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoApiView(APIView):
    """
    Api de Cursos
    """    
    
    def get(self, request):
        print(request.user) 
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoApiView(APIView):
    """
    Api de Avaliação
    """
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    