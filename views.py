from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ProductoForm
from .models import Producto

def MenuInicial(request):
    return render(request, 'app/MenuInicial.html')

def Categoria(request):
    return render(request, 'app/Categoria.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')

def CarroCompra(request):
    return render(request, 'app/CarroCompra.html')

def Donaciones(request):
    return render(request, 'app/Donaciones.html')

def inicioSesion(request):
    return render(request, 'app/inicioSesion.html')

def registro(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        form = ClienteForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"]="Registro exitoso"
        else:
            data["mensaje"]="Error en el registro"
            data["form"]=form
            return redirect('/registro')
    return render(request, 'app/registro.html', data)
    
def agregar(request):
    
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/agregar.html', data)

def listar(request):
    productos = Producto.objects.all()
    
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)

def modificar(request, codigoProducto):
    
    producto = get_object_or_404(Producto, codigoProducto=codigoProducto)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
    if formulario.is_valid():
        formulario.save()
        data["mensaje"] = "Guardado Correctamente"
    else:
        data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html', data)