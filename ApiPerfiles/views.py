from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ApiPerfiles import serializers

class HelloApiView(APIView):
    
    serializer_class = serializers.HelloSerializer
    
    """Clase de una Api de prueba"""
    
    def get(self, request,format=None):
        """ Retornar listas de caracteristicas de APIVies"""
        api=[
            "Usamos metodos http get, post,put,delete",
            "es similar a una vista tradicional de django",
            "nos da un mayor control sobre la logica de nuestra aplicacion",
            "esta mapeado manualmente a los url",
        ]
        return Response({'message':'hello','apiView': api})
    
    def post(self, request):
        """Crea un mensaje con El nombre que le pasamos"""
        
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )
        
    def put(self,request, pk=None):
        """Actualiza un objeto"""
        return Response({'method': 'PUT'})
    
    def path(self, request,pk=None):
        """Actualizacion parcial del objeto"""
        return Response({'method': 'PATCH'})
        
     
    def delete(self, request,pk=None):
        """Eliminacion del objeto"""
        return Response({'method': 'DELETE'})
