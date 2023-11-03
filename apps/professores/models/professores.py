from django.db import models


class Professores(models.Model):

    primeiro_nome = models.CharField('Primeiro Nome', max_length=255, default='Primeiro Nome')
    ultimo_nome = models.CharField('Ultimo Nome', max_length=255, default='Ultimo Nome')
    cpf = models.CharField('CPF', max_length=11, unique=True, help_text='Por favor, digite apenas os números do CPF.', default='00000000000')
    data_nascimento = models.DateField('Data Nascimento', null=True, blank=True)

    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = 'Professores(as)'

    def get_full_name(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome

    def __str__(self):
        return self.get_full_name()