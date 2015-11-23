from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse, HttpRequest
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from .models import Usuarios
from .models import Libros, Categoria
from django.contrib.auth.models import User
from django.core import serializers
from .forms import Libros_Form, ContactoForm
from django.db.models import Q
import re
from django.core.mail import EmailMessage


# Create your views here.
def bienvenido(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/acceso')
	if request.POST:
		titulo = 'Mensaje de Servidor Virtualbooks'
		contenido = 'De: ' + request.POST['nombre'] + '\n' + 'Mensaje:' + '\n' + request.POST['mensaje'] + "\n"
		contenido += 'Comunicarse a:' + ' ' + request.POST['correo']
		correo = EmailMessage(titulo, contenido, to = ['virtualbooks2015@gmail.com'])
		correo.send()
		ctx = {'mensaje':'Mensaje enviado con exito!'}
	else:
		ctx = {'mensaje':'Aun no manda el mensaje.'}
	return render(request, 'index.html', ctx)

def vistainteres(request):
	if not request.user.is_anonymous():
		return render(request,'vistainteres.html')
	else:
		return HttpResponseRedirect('/')

def glosario(request):
	if not request.user.is_anonymous():
		return render(request,'glosario.html')
	else:
		return HttpResponseRedirect('/')

def acerca(request):
	if not request.user.is_anonymous():
		return render(request,'acerca.html')
	else:
		return HttpResponseRedirect('/')

def listado(request):
	lib = Libros.objects.all()
	if not request.user.is_anonymous():
		return render(request,'listado.html',{'lib':lib})
	else:
		return HttpResponseRedirect('/')

def ayuda_noreg(request):
	if request.user.is_anonymous():
		return render_to_response('ayudano_reg.html')
	else:
		return HttpResponseRedirect('/')

def ayuda_reg(request):
	if not request.user.is_anonymous():
		return render(request,'ayuda.html')
	else:
		return HttpResponseRedirect('/')

# def buscarpor(request, a_catego):
# 	p = Libros.objects.get(catego=a_catego)
# 	if request.user.is_anonymous():
# 		return HttpResponseRedirect('/')
# 	if request.method == 'GET':
# 		resul = Libros.objects.filter(lib_categoria=p)
# 		return render(request,'categoria.html',{'p':p, 'resul':resul})
# 	else:
# 		return render(request, 'categoria.html')

def categoria(request, a_catego):
	#p = Libros.objects.get(lib_categoria=a_catego)
	if request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == 'GET':
		a = a_catego
		prueba = Categoria.objects.all().order_by('catego')
		resul = Libros.objects.filter(lib_categoria=a_catego).order_by('lib_titulo')
		return render(request,'categoria.html',{'resul':resul, 'a':a, 'prueba':prueba})
	else:
		return render(request, 'categoria.html')

@login_required(login_url='/acceso')
def logueado(request):
	if request.user.is_superuser:
		usuario = request.user 
		prueba = Categoria.objects.all().order_by('catego')
		ctx = {'prueba':prueba,'usuario':usuario}
		return render(request,('privado_super.html'), ctx)
	else:
		usuario = request.user 
		return render(request,'privado_normal.html',{'usuario':usuario})	

def nuevo_usuario(request):
	if request.user.is_anonymous():
		if request.method=='POST':
			formulario = UserCreationForm(request.POST)
			if User.objects.filter(username=request.POST['username']).exists():
				ctx = {'mensaje':'El usuario ya existe.'}
				return render(request, 'registroof.html',ctx)
			if formulario.is_valid:
				formulario.save()
				return HttpResponseRedirect('/')
		else:
			formulario = UserCreationForm()
	else:
		return HttpResponseRedirect('/acceso')
	return render(request,'registroof.html')

def ingresar(request):
	# if request.user.is_super():
	# 	return render_to_response('superuser.html')
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/bienvenido')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password = clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/acceso')
				else:
					return render_to_response('noactivo.html')
			else:
				#return render_to_response('nousuario.html')
				ctx = {'mensaje':'Usuario y Contrasena no validos.'}
				#formulario = AuthenticationForm()
				return render(request,'loginxd.html',ctx)
	else:
		formulario = AuthenticationForm()
	return render(request,'loginxd.html', {'formulario':formulario})


@login_required(login_url='/acceso')
def registro_libros(request):
	cat = Categoria.objects.all()
	if request.user.is_superuser:
		if request.POST:
			lib_imagen = request.FILES['imagen']
			lib_titulo = request.POST['titulo']
			lib_autor = request.POST['autor']
			lib_categoria = request.POST['categoria']
			lib_descripcion = request.POST['descripcion']
			lib_fecha = request.POST['fecha']
			lib_ver = request.POST['ver']
			lib_descargar = request.POST['descargar']
			Libros.objects.create(lib_imagen=lib_imagen,lib_titulo=lib_titulo,lib_autor=lib_autor,lib_categoria=lib_categoria,lib_descripcion=lib_descripcion,lib_fecha=lib_fecha,lib_ver=lib_ver,lib_descargar=lib_descargar)
			ctx = {'mensaje':'Datos Guardados', 'cat':cat}
		else:
			ctx = {'mensaje':'Registro de Libros', 'cat':cat}
		return render(request,'datoslibro.html',ctx)		
	else:
		return HttpResponseRedirect('/')

# @login_required(login_url='/acceso')
# def privadonormal(request):
# 	usuario = request.user
# 	return render(request,'privado_normal.html',{'usuario':usuario})

# @login_required(login_url='/acceso')
# def privadosuper(request):
# 	usuario = request.user
# 	return render(request,'privado_super.html',{'usuario':usuario})

#@login_required(login_url='/acceso')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def reporte(request):
	usuario = User.objects.all().order_by('username')
	if not request.user.is_anonymous():
		return render_to_response('reporte.html',{'usuario':usuario})
	else:
		return HttpResponseRedirect('/')	


#class BuscarView(TemplateView):
#	template_name='buscar.html'
@login_required(login_url='/acceso')
def post(request, *args, **kwargs):
	if request.POST:
		buscar = request.POST['buscalo']
		libros = Libros.objects.all()
		if libros:
			qset = (
            Q(lib_titulo__contains=buscar) |
            Q(lib_autor__contains=buscar) |
            Q(lib_categoria__contains=buscar) 
           	#Q(lib_descripcion__contains=buscar)
        	)
        	results = Libros.objects.filter(qset).distinct()
    	#else:
        	#results = []
    		return render(request, "buscar.html", {
        		"results": results,
        		"buscar": buscar
   			})
   	else:
   		return render(request,'buscar.html')
		#libros = Libros.objects.filter(lib_titulo__contains=buscar)		return render(request, 'app/buscar.html')		

def contacto(request):
	if not request.user.is_anonymous():
		if request.POST:
			titulo = 'Mensaje de Servidor Virtualbooks'
			contenido = 'De: ' + request.POST['nombre'] + '\n' + 'Mensaje:' + '\n' + request.POST['mensaje'] + "\n"
			contenido += 'Comunicarse a:' + ' ' + request.POST['correo']
			correo = EmailMessage(titulo, contenido, to = ['virtualbooks2015@gmail.com'])
			correo.send()
			ctx = {'mensaje':'Mensaje enviado con exito!'}
		else:
			ctx = {'mensaje':'Aun no manda el mensaje.'}
		return render(request, 'Contacto.html', ctx)
	else:
		return HttpResponseRedirect('/')