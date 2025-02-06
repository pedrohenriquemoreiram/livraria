from rest_framework.viewsets import ModelViewSet

from core.models import Favorito
from core.serializers import FavoritoSerializer, FavoritoRetriveSerializer

class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

    def get_serializer_class(self):
        if self.action in ["retrieve"]:
            return FavoritoRetriveSerializer
        return FavoritoSerializer   
