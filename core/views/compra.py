from rest_framework.viewsets import ModelViewSet
from core.models import Compra
from rest_framework.permissions import IsAuthenticated
from core.serializers import CompraCreateUpdateSerializer, CompraListSerializer, CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario.id)

    def get_serializer_class(self):
        if self.action == "list":
            return CompraListSerializer
        if self.action in ("create", "update"):
            return CompraCreateUpdateSerializer
        return CompraSerializer
    
