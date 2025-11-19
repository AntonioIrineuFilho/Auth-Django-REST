from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioAuthViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['POST'])
    def registro(self, request):

    @action(detail=False, methods=['POST'])
    def login(self, request):

    @action(detail=False, methods=['POST'])
    def logout(self, request):

    @action(detail=True, methods=['GET', 'PUT'])
    def perfil(self, request):
