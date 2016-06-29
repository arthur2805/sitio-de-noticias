#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
	titulo = models.CharField(max_length=100, verbose_name='Título De Noticia', unique=True)
	noticia = models.TextField(help_text='Reporte Completo De La Noticia')
	imagen = models.ImageField(upload_to='noticias', verbose_name='Fotografias a Adjuntar')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia)
    texto = models.TextField(help_text='', verbose_name='Comentario')

    def __unicode__(self):
        return self.texto
