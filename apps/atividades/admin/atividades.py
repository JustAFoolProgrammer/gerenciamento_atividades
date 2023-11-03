from django.contrib import admin
from ..models import Atividades

@admin.register(Atividades)
class AtividadesAdmin(admin.ModelAdmin):
    model = Atividades
    list_display_links = ['nome']
    list_display = ('nome', 'quantidade_alunos', 'responsavel', 'dias_semana')
    search_fields = ['nome']
    list_per_page = 10
    fieldsets = (
        ('Geral', {
            'fields': ('nome', 'quantidade_alunos', 'responsavel', 'dias_semana')
        }),
    )