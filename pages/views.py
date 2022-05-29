from django.shortcuts import render

from .models import ApresentacaoPesquisa, SlidesPesquisa


def index(request):

    data = {}
    data['apresentacao_pesquisa'] = ApresentacaoPesquisa.objects.all()
    data['slides_pesquisa'] = SlidesPesquisa.objects.all()


    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')