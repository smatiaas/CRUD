from django import forms
from.models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields = ['usuarioCliente', 'nombreCliente', 'contrasenaCliente', 'contrasenaCliente2', 'emailCliente', 'telefonoCliente', 'aceptoCliente']	

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        
    
