from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Membros
from .serializers import MembrosSerializer

class MembrosListView(APIView):
    """
    Listar todos os membros
    """
    def get(self, request, *args, **kwargs):
        membros = Membros.objects.all()
        serializer = MembrosSerializer(membros, many=True)
        return Response({
            'membros': serializer.data
        }, status=status.HTTP_200_OK)

class MembrosCreateView(APIView):
    """
    Criar um novo membro
    """
    def post(self, request, *args, **kwargs):
        serializer = MembrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Membro criado com sucesso!',
                'membro': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembrosRetrieveView(APIView):
    """
    Obter detalhes de um membro específico
    """
    def get_object(self, pk):
        try:
            return Membros.objects.get(pk=pk)
        except Membros.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        membro = self.get_object(pk)
        if membro is None:
            return Response({'message': 'Membro não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MembrosSerializer(membro)
        return Response({
            'message': 'Detalhes do membro',
            'membro': serializer.data
        }, status=status.HTTP_200_OK)

class MembrosUpdateView(APIView):
    """
    Atualizar um membro específico
    """
    def get_object(self, pk):
        try:
            return Membros.objects.get(pk=pk)
        except Membros.DoesNotExist:
            return None

    def put(self, request, pk, *args, **kwargs):
        membro = self.get_object(pk)
        if membro is None:
            return Response({'message': 'Membro não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MembrosSerializer(membro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Membro atualizado com sucesso!',
                'membro': serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        membro = self.get_object(pk)
        if membro is None:
            return Response({'message': 'Membro não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MembrosSerializer(membro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembrosDeleteView(APIView):
    """
    Excluir um membro específico
    """
    def get_object(self, pk):
        try:
            return Membros.objects.get(pk=pk)
        except Membros.DoesNotExist:
            return None

    def delete(self, request, pk, *args, **kwargs):
        membro = self.get_object(pk)
        if membro is None:
            return Response({'message': 'Membro não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        membro.delete()
        return Response({'message': 'Membro excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
