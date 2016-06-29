from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^noticias/$','principal.views.lista_noticias'),
    url(r'^noticia/(?P<id_noticia>\d+)$','principal.views.detalle_noticia'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^noticia/nueva/$','principal.views.nueva_noticia'),
    url(r'^comenta/$','principal.views.nuevo_comentario'),
    
)
