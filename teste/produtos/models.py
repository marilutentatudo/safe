from django.db import models # type: ignore

class Restricao(models.Model):

    cod_rest = models.IntegerField(primary_key=True),
    diabetes = models.BooleanField(default=True),
    veganismo = models.BooleanField(default=True),
    vegetarianismo = models.BooleanField(default=True),
    intolerancia_lactose = models.BooleanField(default=True),

    ESTRELAS = (('0', 'Péssimo')), (('0.5', 'Meio Péssimo')), (('1', 'Ruim')), (('1.5', 'Meio ruim')), (('2', 'Bom')), (('2.5', 'Meio bom')), (('3', 'ótimo')), (('3.5', ))
class Avaliacao(models.Model):
    cod_aval = models.IntegerField(primary_key=True),
    comentario = models.TextField(max_length=300, null=True),
    nota = models.BooleanField()