"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from app.views import BuscarView

urlpatterns = [
    url(r'^$', 'app.views.bienvenido'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^acceso/$','app.views.ingresar'),
    url(r'^acerca/$','app.views.acerca'),
    url(r'^ayuda_reg/$','app.views.ayuda_reg'),
    url(r'^ayuda_noreg/$','app.views.ayuda_noreg'),
    url(r'^bienvenido/$', 'app.views.logueado'),
    url(r'^buscar/$', 'app.views.post', name='buscar'),
    url(r'^cerrar/$', 'app.views.cerrar'),
    url(r'^categoria/(?P<a_catego>.*)/$', 'app.views.categoria', name='categoria'),
    url(r'^contacto/$','app.views.contacto'),
    url(r'^interes/$','app.views.vistainteres'),
    url(r'^glosario/$','app.views.glosario'),
    url(r'^listado/$','app.views.listado'),
    url(r'^registro/$', 'app.views.nuevo_usuario'),
    url(r'^uploads/$', 'app.views.registro_libros', name="uploads"),
    url(r'^usuarios/$', 'app.views.reporte'),
    url(r'^weblibros/$','WebService.views.wsLibros'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    #url(r'^$', 'app.views.ingreso'),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )