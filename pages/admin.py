from django.contrib import admin

from .models import ApresentacaoPesquisa, GuiaVideos, Hero, SlidesPesquisa, TiposViolencia

admin.site.register(Hero)

admin.site.register(ApresentacaoPesquisa)

admin.site.register(SlidesPesquisa)

admin.site.register(GuiaVideos)

admin.site.register(TiposViolencia)