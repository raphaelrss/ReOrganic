from django.contrib import admin

from core.models import User, Endereco, Categoria, Compost, Post, Entrega, Coleta, Troca, Avaliacao

# Register your models here.
admin.site.register(User)
admin.site.register(Endereco)
admin.site.register(Categoria)
admin.site.register(Compost)
admin.site.register(Post)
admin.site.register(Entrega)
admin.site.register(Coleta)
admin.site.register(Troca)
admin.site.register(Avaliacao)
