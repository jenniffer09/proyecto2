"""nomina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mtto.views import inicio, crearCargo,editarCargo,eliminarCargo,crearDepartamento,editarDepartamento,eliminarDepartamento,crearEmpleado,editarEmpleado,eliminarEmpleado
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio" ),
    path('cargo/',crearCargo,name="cargo" ),
    path('editar_cargo/<int:id>', editarCargo, name="editar_cargo"),
    path('eliminar_cargo/<int:id>', eliminarCargo, name='eliminar_cargo'),
    path('dpto/',crearDepartamento,name="departamento" ),
    path('editar_departamento/<int:id>', editarDepartamento, name="editar_departamento"),
    path('eliminar_departamento/<int:id>', eliminarDepartamento, name='eliminar_departamento'),
    path('empleado/',crearEmpleado,name="empleado" ),
    path('editar_empleado/<int:id>', editarEmpleado, name="editar_empleado"),
    path('eliminar_empleado/<int:id>', eliminarEmpleado, name='eliminar_empleado'),
]
