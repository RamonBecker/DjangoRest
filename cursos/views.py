"""
***************************************************************************

API V1

***************************************************************************
"""

from rest_framework.generics import get_object_or_404
from rest_framework import generics, mixins, serializers

from .models import Curso, Avaliacao

from .serializers import CursoSerializer, AvaliacaoSerializer




class CursosApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    
class CursoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    

class AvaliacoesApiView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer 
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))

        return self.queryset.all()

class AvaliacaoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer 

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
***************************************************************************

API V2

***************************************************************************
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response  
from rest_framework import permissions
from .permissions import EhSuperUser



class CursoViewSet(viewsets.ModelViewSet):
    
    #O django irá verificar qual permissão vai se encaixar na hora de o usuário fazer uma solicitação de um recurso. A verificação ocorrerá da seguinte forma: 
    # Se o usuário se encaixar na permissão de EhSuperUser o django vai usar esta permissão, caso contrário ele irá para a seguinte permissão: Django Model Permissions e assim sucessivamente
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions, 
    )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        
        #Paginação
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    

""" 
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

class AvaliacaoViewSet(
 #   mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    
    queryset= Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer