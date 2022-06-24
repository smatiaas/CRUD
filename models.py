from django.db import models

class EncargadoPerro(models.Model):
    nombreEncargado = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreEncargado
    
class Perro(models.Model):
    nombrePerro = models.CharField(max_length=50)
    razaPerro = models.TextField()
    peso = models.IntegerField()
    castrado = models.BooleanField()
    encargado = models.ForeignKey(EncargadoPerro, on_delete=models.PROTECT)
    fechaNacimiento = models.DateField()
    
    def __str__(self):
        return self.nombrePerro
    
class Cliente(models.Model):
    usuarioCliente = models.CharField(max_length=50)
    nombreCliente = models.CharField(max_length=50)
    contrasenaCliente = models.CharField(max_length=50)
    contrasenaCliente2 = models.CharField(max_length=50)
    emailCliente= models.EmailField()
    telefonoCliente = models.CharField(max_length=10) 
    aceptoCliente= models.BooleanField()
    
    def __str__(self):
        return self.nombreCliente
    
class Producto(models.Model):
    codigoProducto = models.IntegerField('Codigo Producto')
    nombreProducto = models.CharField('Nombre Producto',max_length=50)
    precioProducto = models.IntegerField('Precio')
    descripcionProducto = models.CharField('Descripción',max_length=200)
    
    def __str__(self):
        return self.nombreProducto
    