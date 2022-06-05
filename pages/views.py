from django.shortcuts import render

from .models import ApresentacaoPesquisa, GuiaVideos, Hero, SlidesPesquisa, TiposViolencia


def index(request):

    data = {}
    data['apresentacao_pesquisa'] = ApresentacaoPesquisa.objects.all()
    data['slides_pesquisa'] = SlidesPesquisa.objects.all()
    data['guia_videos'] = GuiaVideos.objects.all()
    data['tipos_violencia'] = TiposViolencia.objects.all()


    return render(request, 'index.html', data)


def home(request):

    data = {}
    data['hero'] = Hero.objects.all()
    data['apresentacao_pesquisa'] = ApresentacaoPesquisa.objects.all()
    data['slides_pesquisa'] = SlidesPesquisa.objects.all()
    data['guia_videos'] = GuiaVideos.objects.all()
    data['tipos_violencia'] = TiposViolencia.objects.all()


    return render(request, 'template.html', data)


def about(request):
    return render(request, 'about.html')

def page_text(request):
    return render(request, 'pagina_texto.html')

def page_text_two(request):
    return render(request, 'pagina_texto_two.html')

def page_text_three(request):
    return render(request, 'pagina_texto_three.html')