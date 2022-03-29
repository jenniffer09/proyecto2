from urllib.request import Request
from django.shortcuts import redirect, render,HttpResponse
from mtto.forms import CargoForm, DepartamentoFrom, EmpleadoFrom


from .models import Cargo, Departamento, Empleado

def inicio(request):
   
    return render(request, "index.htm")
def empleado(request):

    return render(request,"pages/empleado.htm")

def crearCargo(request):
    if request.method == "POST":
        print("entro por post")
       
        cargo_form = CargoForm(request.POST)
        
        if cargo_form.is_valid():
           
            cargo_form.save()
    else: 
        print("entro por get")  
       
    cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/cargo.htm", {'cargoForm': cargo_form, 'cargos':cargos, 'accion':'Crear'})
    

def editarCargo(request,id):
    
    error,cargo_form=None,None
    try:
        
        cargo = Cargo.objects.get(id=id)
        if request.method == "GET":
           cargo_form = CargoForm(instance=cargo) 
        else:
           cargo_form = CargoForm(request.POST,instance=cargo)
           if cargo_form.is_valid():
                
                cargo_form.save()
                
                return redirect('cargo') 
    except Exception as e:
        error=e 
   
    cargos = Cargo.objects.all()
    return render(request, "pages/cargo.htm", {'cargoForm': cargo_form, 'cargos':cargos, 'accion':'Actualizar'})

def eliminarCargo(request,id):
 
    cargo = Cargo.objects.get(id=id)
    if request.method == 'POST':
     
        cargo.delete()    
        
        return redirect("cargo")
    return render(request,'pages/eliminar_cargo.htm',{'cargo':cargo})  

def crearDepartamento(request):
    if request.method == "POST":
        print("entro por post")
       
        departamento_form = DepartamentoFrom(request.POST)
      
        if departamento_form.is_valid():
           
            departamento_form.save()
    else: 
        print("entro por get")  
       
    departamento_form = DepartamentoFrom()
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.htm", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion':'Crear'})
    

def editarDepartamento(request,id):
    
    error,departamento_form=None,None
    try:
        
        departamento = Departamento.objects.get(id=id)
        if request.method == "GET":
           departamento_form = DepartamentoFrom(instance=departamento) 
        else:
           departamento_form = DepartamentoFrom(request.POST,instance=departamento)
           if departamento_form.is_valid():
                
                departamento_form.save()
                
                return redirect('departamento') 
    except Exception as e:
        error=e 
   
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.htm", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion':'Actualizar'})

def eliminarDepartamento(request,id):
 
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
       
        departamento.delete()    
        
        return redirect("departamento")
    return render(request,'pages/eliminar_departamento.htm',{'departamento':departamento})

def crearEmpleado(request):
    if request.method == "POST":
        print("entro por post")
        
        empleado_form = EmpleadoFrom(request.POST)
        
        if empleado_form.is_valid():
            
            empleado_form.save()
    else: 
        print("entro por get")  
       
    empleado_form = EmpleadoFrom()
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.htm", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion':'Crear'})
    

def editarEmpleado(request,id):
   
    error,empleado_form=None,None
    try:
        
        empleado = Empleado.objects.get(id=id)
        if request.method == "GET":
           empleado_form = EmpleadoFrom(instance=empleado) 
        else:
           empleado_form = EmpleadoFrom(request.POST,instance=empleado)
           if empleado_form.is_valid():
             
                empleado_form.save()
               
                return redirect('empleado') 
    except Exception as e:
        error=e 
   
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.htm", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion':'Actualizar'})

def eliminarEmpleado(request,id):
    
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
       
        empleado.delete()    
       
        return redirect("empleado")
    return render(request,'pages/eliminar_empleado.htm',{'empleado':empleado})