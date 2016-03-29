# -*- encoding: utf-8 -*-
from django.forms import ModelForm, TextInput
from django import forms
from .models import Independiente,Servicio


class DetalleIndependienteForm(forms.ModelForm):
    class Meta:
        model = Independiente
        fields = '__all__'
        labels = {
            'idServicio':'Servicio',
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'aniosExperiencia':'Años de experiencia',
            'telefono':'Teléfono',
            'correoElectronico':'Correo Electronico',
            'fechaRegistro':'Fecha Registro',
        }
        exclude = ['contrasenia']
        widgets = {
            'nombre': TextInput(attrs={'readonly':'readonly'}),
            'apellidos': TextInput(attrs={'readonly':'readonly'}),
            'idServicio': TextInput(attrs={'readonly':'readonly'}),
            'aniosExperiencia': TextInput(attrs={'readonly':'readonly'}),
            'telefono': TextInput(attrs={'readonly':'readonly'}),
            'correoElectronico': TextInput(attrs={'readonly':'readonly'}),
            'foto': TextInput(attrs={'readonly':'readonly'}),
            'foto': forms.HiddenInput()
        }


class IndependienteForm(forms.ModelForm):
   class Meta:
        model = Independiente
        fields = '__all__'
        labels = {
            'idServicio':'Servicio',
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'aniosExperiencia':'Años de experiencia',
            'telefono':'Teléfono',
            'correoElectronico':'Correo Electronico',
            'fechaRegistro':'Fecha Registro',
        }
        exclude = ['contrasenia', 'idServicio']
        widgets = {
            'correoElectronico': TextInput(attrs={'readonly':'readonly'}),
            'foto': forms.HiddenInput()
        }

        owner = forms.ModelChoiceField(label="Servicio2",
                                  queryset=Servicio.objects.all())

