from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra, ItensCompra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True) 
    status = CharField(source="get_status_display", read_only=True) # inclua essa linha
    itens = ItensCompraSerializer(many=True, read_only=True)


class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"