from django.forms import ModelForm
from .models import Cliente

class ClienteForm (ModelForm):

	class Meta:
		model = Cliente
		fields = ['nomecompleto', 'nascimento', 'sexo', 'whatsapp','endereco', 'cidade', 'email']
