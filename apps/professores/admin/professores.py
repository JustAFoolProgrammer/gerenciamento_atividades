from django.contrib import admin
from ..models import Professores


@admin.register(Professores)
class ProfessoresAdmin(admin.ModelAdmin):
    model = Professores
    list_display_links = 'primeiro_nome',
    list_display = ('primeiro_nome', 'ultimo_nome', 'cpf', 'data_nascimento')
    search_fields = ['cpf']
    list_per_page = 10
    fieldsets = (
        ('Geral', {
            'fields': ('primeiro_nome', 'ultimo_nome', 'cpf', 'data_nascimento')
        }),
    )