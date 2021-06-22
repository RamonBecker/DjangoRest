import re
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #verificando se os dados enviado são válidos, caso contrário manda uma exceção
        serializer.save()
        #return Response({"msg": "Criou com sucesso"}, status.HTTP_201_CREATED)
        #return Response({"id": serializer.data['id'], 
                         #"curso": serializer.data['titulo']}, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_201_CREATED)

class AvaliacaoApiView(APIView):
    """
    Api de Avaliação
    """
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)