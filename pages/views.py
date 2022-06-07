from pyexpat import model
from django.shortcuts import render

from .models import ApresentacaoPesquisa, GuiaVideos, Hero, LinksExternos, SlidesPesquisa, SobreMetodologia, SobrePesquisa, SobrePesquisadora, TiposViolencia


def index(request):

    data = {}
    data['apresentacao_pesquisa'] = ApresentacaoPesquisa.objects.all()
    data['slides_pesquisa'] = SlidesPesquisa.objects.all()
    data['guia_videos'] = GuiaVideos.objects.all()
    data['tipos_violencia'] = TiposViolencia.objects.all()


    return render(request, 'index.html', data)


def home(request):

    data = {}
    data['apresentacao_pesquisa'] = ApresentacaoPesquisa.objects.all()
    data['slides_pesquisa'] = SlidesPesquisa.objects.all()
    data['guia_videos'] = GuiaVideos.objects.all()
    data['tipos_violencia'] = TiposViolencia.objects.all()
    data['links_externos'] = LinksExternos.objects.all()


    return render(request, 'template.html', data)


def about(request):

    data = {}
    data['sobre_pesquisa'] = SobrePesquisa.objects.first()
    data['sobre_metodologia'] = SobreMetodologia.objects.first()
    data['sobre_pesquisadora'] = SobrePesquisadora.objects.first()


    return render(request, 'about.html', data)

def page_text(request):
    return render(request, 'pagina_texto.html')

def page_text_two(request):
    return render(request, 'pagina_texto_two.html')

def page_text_three(request):
    return render(request, 'pagina_texto_three.html')