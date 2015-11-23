from django import forms

class Libros_Form(forms.ModelForm):
	lib_imagen = forms.ImageField()
	lib_titulo = forms.CharField(widget= forms.TextInput())
	lib_autor = forms.CharField(widget= forms.TextInput())
	lib_categoria = forms.CharField(widget= forms.TextInput())
	lib_descripcion = forms.CharField(widget= forms.TextInput())
	lib_fecha = forms.DateField(widget= forms.DateInput())

class ContactoForm(forms.Form):
	nombre = forms.CharField(widget = forms.TextInput())
	correo = forms.EmailField(label='Correo:')
	mensaje = forms.CharField(widget=forms.Textarea)
	
		