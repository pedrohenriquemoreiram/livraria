from rest_framework.serializers import ModelSerializer

from core.models import Favorito

class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = "__all__"
        
        

class FavoritoRetriveSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = "__all__"
        depth = 1