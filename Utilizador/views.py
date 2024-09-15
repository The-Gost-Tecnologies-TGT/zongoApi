import logging
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



logger = logging.getLogger(__name__)


@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

        
User = get_user_model()

class UserLoginGerar1(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email e senha são obrigatórios'}, status=400)

        # Autenticar o usuário com as credenciais fornecidas
        user = authenticate(request, email=email, password=password)

        if user:
            # Gera ou obtém o token para o usuário autenticado
            token, _ = Token.objects.get_or_create(user=user)

            # Retorna os dados do usuário
            response_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'token': token.key,
            }

            return Response(response_data, status=200)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=401)


class UserLogout(APIView):
    def post(self, request):
        token_key = request.data.get('token')

        if not token_key:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = Token.objects.get(key=token_key)
            token.delete()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class UserCreateView(APIView):
    """
    Criar um novo usuário
    """
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Usuário criado com sucesso!',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserListView(generics.ListAPIView):
    """
    Listar todos os usuários
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDeleteView(APIView):
    """
    Excluir um usuário específico
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def delete(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if user is None:
            return Response({'message': 'Usuário não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response({'message': 'Usuário excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    
    
class UserUpdateView(APIView):
    """
    Atualizar um usuário específico
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def put(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if user is None:
            return Response({'message': 'Usuário não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Usuário atualizado com sucesso!',
                'user': serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)