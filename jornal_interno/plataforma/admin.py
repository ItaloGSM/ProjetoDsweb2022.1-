from django.contrib import admin

from plataforma.models import Colunista, Comentario, Edicao, Noticia

admin.site.register(Colunista)
admin.site.register(Edicao)
admin.site.register(Noticia)
admin.site.register(Comentario)

