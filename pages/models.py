from pyexpat import model
from django.db import models




class Hero(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=150)
    texto_auxiliar = models.CharField(max_length=485)
    ultimo_texto = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Hero"

    def __str__(self) -> str:
        return self.titulo


class ApresentacaoPesquisa(models.Model):
    primeiro_texto = models.CharField(max_length=50)
    segundo_texto = models.CharField(max_length=50)
    terceiro_texto = models.TextField(max_length=400)
    quarto_texto = models.TextField(max_length=400)
    imagem = models.ImageField(upload_to="imagem//%Y/%m/%d", blank=True)

    class Meta:
        verbose_name = "Apresentação Pesquisa"
        verbose_name_plural = "Apresentação Pesquisa"

    def __str__(self) -> str:
        return self.segundo_texto


class SlidesPesquisa(models.Model):
    primeiro_texto = models.CharField(max_length=50)
    segundo_texto = models.CharField(max_length=50)
    terceiro_texto = models.TextField(max_length=400)
    quarto_texto = models.TextField(max_length=400)
    quinto_texto = models.TextField(max_length=400)
    imagem = models.ImageField(upload_to="imagem_slide//%Y/%m/%d", blank=True)


    class Meta:
        verbose_name = "Slides Pesquisa"
        verbose_name_plural = "Slides Pesquisa"

    def __str__(self) -> str:
        return self.segundo_texto

    
class GuiaVideos(models.Model):
    primeiro_texto = models.CharField(max_length=150)
    segundo_texto = models.CharField(max_length=250)
    terceiro_texto = models.TextField(max_length=400)
    link = models.TextField(max_length=400)

    class Meta:
        verbose_name = "Guia Videos"
        verbose_name_plural = "Guia Videos"

    def __str__(self) -> str:
        return self.primeiro_texto

class TiposViolencia(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=400)

    class Meta:
        verbose_name = "Tipos Violência"
        verbose_name_plural = "Tipos Violência"

    def __str__(self) -> str:
        return self.nome

class LinksExternos(models.Model):
    texto = models.CharField(max_length=150)
    tag_classe = models.CharField(max_length=150)
    link = models.CharField(max_length=350)

    class Meta:
        verbose_name = "Links Externos"
        verbose_name_plural = "Links Externos"

    def __str__(self) -> str:
        return self.texto

class SobrePesquisa(models.Model):
    texto = models.TextField(max_length=550)

    class Meta:
        verbose_name = "Sobre Pesquisa"
        verbose_name_plural = "Sobre Pesquisa"

    def __str__(self) -> str:
        return self.texto

class SobreMetodologia(models.Model):
    texto = models.TextField(max_length=550)

    class Meta:
        verbose_name = "Sobre Metodologia"
        verbose_name_plural = "Sobre Metodologia"

    def __str__(self) -> str:
        return self.texto

class SobrePesquisadora(models.Model):
    texto = models.TextField(max_length=550)

    class Meta:
        verbose_name = "Sobre Pesquisadora"
        verbose_name_plural = "Sobre Pesquisadora"
    def __str__(self) -> str:
        return self.texto

