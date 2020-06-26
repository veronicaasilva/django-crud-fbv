from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outros', 'Outros')
    ]
    nomecompleto = models.CharField('Nome Completo', max_length=150)
    nascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=9, choices=SEXO_CHOICES)
    whatsapp = models.CharField('Whatsapp', max_length=15)
    endereco = models.CharField('Endereço', max_length=150)
    cidade = models.CharField('Cidade', max_length=30)
    email = models.EmailField('Email')

    def __str__(self):
        return self.nomecompleto
