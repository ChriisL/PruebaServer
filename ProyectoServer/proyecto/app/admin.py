from django.contrib import admin
from .models import Usuarios
from .models import Libros, Categoria
#from .models import Ponentes
#from .models import Staff
# Register your models here.
admin.site.register(Usuarios)
#admin.site.register(Libros)
@admin.register(Libros)
class Libros_admin(admin.ModelAdmin):
	list_display = ('lib_titulo', 'lib_autor','lib_categoria','lib_descripcion','lib_fecha','lib_ver','lib_descargar','lib_imagen','thumbnail')
	list_filter = ('lib_titulo',)
	search_fields = ('lib_titulo','lib_autor',)

@admin.register(Categoria)
class Categoria_admin(admin.ModelAdmin):
	list_display = ('catego', 'id_catego',)
	list_filter = ('catego',)
	#search_fields = ('lib_titulo','lib_autor',)