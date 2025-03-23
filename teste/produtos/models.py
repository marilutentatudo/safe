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
    nota = models.BooleanField()from django.db import models # type: ignore

class Restricao(models.Model):

    cod_rest = models.IntegerField(primary_key=True),
    diabetes = models.BooleanField(default=True),
    veganismo = models.BooleanField(default=True),
    vegetarianismo = models.BooleanField(default=True),
    intolerancia_lactose = models.BooleanField(default=True),

    ESTRELAS = (('0', 'Péssimo')), (('0.5', 'Pouco péssimo')), (('1', 'Ruim')), (('1.5', 'Pouco ruim')), (('2', 'Pouco bom')), (('2.5', 'Bom')), (('3', 'Pouco ótimo')), (('3.5', 'Ótimo')), (('4', 'Pouco excelente')), (('4.5', 'Excelente')), (('5', 'Perfeito'))
class Avaliacao(models.Model):
    cod_aval = models.IntegerField(primary_key=True),
    comentario = models.TextField(max_length=300, null=True),
    nota = models.BooleanField(choices=ESTRELAS, max_length=10),

class UsuarioPessoaFisica(models.Model):
    cod_cpf = models.BigIntegerField(primary_key=True, max_length=11),
    nome = models.CharField(max_length=50, null= False),
    email = models.EmailField(null= False),
    senha = models.TextField(null=False),
    diabetes = models.BooleanField(default=True),
    veganismo = models.BooleanField(default=True),
    vegetarianismo = models.BooleanField(default=True),
    intolerancia_lactose = models.BooleanField(default=True),

class UsuarioPessoaJuridica(models.Model):
    cod_cnpj = models.BigIntegerField(primary_key=True, max_length=14),
    nome = models.CharField(max_length=50, null= False),
    email = models.EmailField(null= False),
    senha = models.TextField(null=False),
    telefone - models.BigIntegerField(max_length=14, null=False),
    endereco = models.TextField(null=False),

class Cardapio(models.Model):
    cod_card = models.AutoField(primary_key=True),
    cardapio = models.FileField(),

class Estabelecimento(models.Model):
    cod_estab = models.AutoField(primary_key=True),
    nome = models.TextField(null=False),
    hora_abertura = models.DateTimeField(null=False),
    hora_encerramento = models.DateTimeField(null=False),
    endereco = models.TextField(null=False),

