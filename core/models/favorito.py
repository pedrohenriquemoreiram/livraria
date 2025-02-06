from django.db import models
from core.models import User
from core.models import Livro

class Favorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="favoritos")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="favoritos")