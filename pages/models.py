from pyexpat import model
from django.db import models


class ApresentacaoPesquisa(models.Model):
    primeiro_texto = models.CharField(max_length=50)
    segundo_texto = models.CharField(max_length=50)
    terceiro_texto = models.TextField(max_length=400)
    quarto_texto = models.TextField(max_length=400)
    imagem = models.ImageField(upload_to="imagem//%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return self.segundo_texto


class SlidesPesquisa(models.Model):
    primeiro_texto = models.CharField(max_length=50)
    segundo_texto = models.CharField(max_length=50)
    terceiro_texto = models.TextField(max_length=400)
    quarto_texto = models.TextField(max_length=400)
    quinto_texto = models.TextField(max_length=400)
    imagem = models.ImageField(upload_to="imagem_slide//%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return self.segundo_texto


class GuiaVideos(models.Model):
    primeiro_texto = models.CharField(max_length=150)
    segundo_texto = models.CharField(max_length=250)
    terceiro_texto = models.TextField(max_length=400)
    video = models.FileField(upload_to='videos_uploaded',null=True)

    def __str__(self) -> str:
        return self.primeiro_texto

class TiposViolencia(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=400)

    def __str__(self) -> str:
        return self.nome