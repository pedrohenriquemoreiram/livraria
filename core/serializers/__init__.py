from .user import UserSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import LivroListRetrieveSerializer, LivroSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
from .compra import (
    CompraListSerializer, # novo
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, # novo
    ItensCompraSerializer,
)

from .favorito import FavoritoSerializer

from .livro import (
    LivroAjustarEstoqueSerializer, # novo
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)