from django.contrib import admin

from .models import ApresentacaoPesquisa, GuiaVideos, SlidesPesquisa, TiposViolencia

admin.site.register(ApresentacaoPesquisa)

admin.site.register(SlidesPesquisa)

admin.site.register(GuiaVideos)

admin.site.register(TiposViolencia)