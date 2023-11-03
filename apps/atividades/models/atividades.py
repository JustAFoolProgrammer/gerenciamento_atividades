from django.db import models
from ...professores.models import Professores


class Atividades(models.Model):

    nome = models.CharField('Nome da Atividade', max_length=255, default='Minha Atividade')
    quantidade_alunos = models.IntegerField('Quantidade de alunos', default=1)
    responsavel = models.ForeignKey(Professores, on_delete=models.SET_NULL, related_name='fk_professor', verbose_name='Responsável', null=True, blank=True)
    dias_semana = models.CharField('Dias da Semana', max_length=255, default='Segunda, Quarta, Sexta', help_text='Escreva os dias da semana em que a atividade é realizada.')

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    
    def __str__(self):
        return self.nome
