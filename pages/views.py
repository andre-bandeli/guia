from django.shortcuts import render

from .models import ApresentacaoPesquisa, GuiaVideos, SlidesPesquisa, TiposViolencia


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


    return render(request, 'template.html', data)


def about(request):
    return render(request, 'about.html')