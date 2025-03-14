from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import Specialist, User
from core.serializers import SpecialistSerializer


class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['user__name']


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if password != confirm_password:
        return Response({"error": "As senhas não coincidem"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Usuário já existe"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "Usuário criado com sucesso"}, status=status.HTTP_201_CREATED)
