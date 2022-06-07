from django.contrib import admin

from .models import ApresentacaoPesquisa, GuiaVideos, Hero, LinksExternos, SlidesPesquisa, SobreMetodologia, SobrePesquisa, SobrePesquisadora, TiposViolencia

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "subtitulo"]


@admin.register(ApresentacaoPesquisa)
class ApresentacaoPesquisaAdmin(admin.ModelAdmin):
    list_display = ["primeiro_texto", "segundo_texto"]


@admin.register(SlidesPesquisa)
class SlidesPesquisaAdmin(admin.ModelAdmin):
    list_display = ["primeiro_texto", "segundo_texto"]

@admin.register(GuiaVideos)
class GuiaVideosAdmin(admin.ModelAdmin):
    list_display = ["primeiro_texto", "link"]

@admin.register(TiposViolencia)
class TiposViolenciaAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao"]


admin.site.register(LinksExternos)
admin.site.register(SobrePesquisa)
admin.site.register(SobreMetodologia)
admin.site.register(SobrePesquisadora)