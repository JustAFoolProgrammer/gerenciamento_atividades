from django.contrib import admin
from ..models import Alunos 

@admin.register(Alunos)
class AlunosAdmin(admin.ModelAdmin):
    model = Alunos
    list_display_links = ['nome']
    list_display = ('nome', 'sobrenome', 'esporte', 'genero', 'deficiencia')
    search_fields = ['nome', 'sobrenome', 'esporte']
    list_per_page = 10
    fieldsets = (
        ('Dados do Aluno', {
            'fields': ('nome', 'sobrenome', 'cpf', 'data_nascimento', 'genero', 'telefone', 'email', 'deficiencia')
        }),
        ('Especificações da Atividade', {
            'fields': ('esporte', 'ja_praticou')
        }),
    )