from django.shortcuts import render
from app.models import Libros

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

def wsLibros(request):
	if request.user.is_superuser:
		data = serializers.serialize('json', Libros.objects.all())
		return HttpResponse(data, content_type='application/json')
	else:
		return HttpResponseRedirect('/')