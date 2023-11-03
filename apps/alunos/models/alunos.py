from collections.abc import Iterable
from django.db import models
from django.conf import settings
from ...atividades.models import Atividades



class Alunos(models.Model):

    GENEROS = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro'),
    ]

    nome = models.CharField('Nome', max_length=255, default='Meu Nome')
    sobrenome = models.CharField('Sobrenome', max_length=255, default='Meu Sobrenome')
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, unique=True, help_text='Por favor, digite apenas os números do CPF.', default='00000000000')
    esporte = models.ForeignKey(Atividades, verbose_name='Esporte', on_delete=models.SET_NULL, default='Futebol', related_name='atividade_aluno', null=True)
    telefone = models.CharField('Telefone', max_length=18, null=True, blank=True, help_text='Ex: (16) 99999-9999')
    email = models.EmailField('E-Mail', max_length=255, null=True, blank=True)
    genero = models.CharField('Gênero', max_length=255, default='Masculino', choices=GENEROS)
    deficiencia = models.CharField('PCD?', max_length=255, default='Não', choices=[('Sim', 'Sim'), ('Não', 'Não')])
    ja_praticou = models.CharField('Já praticou o esporte?', max_length=255, default='Não', choices=[('Sim', 'Sim'), ('Não', 'Não')])

    class Meta:
        verbose_name = 'Aluno(a)'
        verbose_name_plural = 'Alunos(as)'

    def get_full_name(self):
        return self.nome + ' ' + self.sobrenome

    def __str__(self):
        return self.get_full_name()
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.esporte.quantidade_alunos += 1
            self.esporte.save()
        return super().save(force_insert, force_update, using, update_fields)