from django.conf.urls import include, url
from .views import Index

urlpatterns = [
    #url(r'^$', 'aplicacion.views.login'),
    url(r'^Bienvenido/$', 'app.views.Logueado'),
    url('', include ('social.apps.django_app.urls', namespace= 'social')),
    url(r'^$', Index.as_view(), name='index'),
]