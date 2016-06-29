#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from principal.models import Noticia, Comentario

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
