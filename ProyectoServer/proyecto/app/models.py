from django.db import models

# Create your models here.
class Usuarios(models.Model):
	usuario_nombre = models.CharField(max_length=60)
	usuario_direccion = models.CharField(max_length=100)
	usuario_correo = models.CharField(max_length=100)
	#usuario_pass = models.PasswordField(max_length=20)
	def __unicode__(self):
		return "Nombre: %s; Direccion: %s;Correo: %s"%(self.usuario_nombre,self.usuario_direccion,self.usuario_correo)

class Libros(models.Model):
	lib_imagen = models.ImageField(upload_to='libros/')
	lib_titulo = models.CharField(max_length=200)
	lib_autor = models.CharField(max_length=200)
	lib_categoria = models.CharField(max_length=100)
	lib_descripcion = models.TextField(max_length=500)
	lib_fecha = models.DateField(auto_now_add=True)
	lib_ver = models.CharField(max_length=500)
	lib_descargar = models.CharField(max_length=500)
	# def __unicode__(self):
	#  	return self.lib_imagen; "Titulo: %s; Autor: %s;Categoria: %s;Descripcion: %s;Fecha: %s"%(self.lib_titulo,self.lib_autor,self.lib_categoria,self.lib_descripcion,self.lib_fecha)
	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width="500"/></a>'%(self.lib_imagen,self.lib_imagen)
	thumbnail.allow_tags=True

class Categoria(models.Model):
	catego = models.CharField(max_length=200)
	id_catego = models.CharField(max_length=200)