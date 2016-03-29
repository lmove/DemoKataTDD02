import sendgrid
import os
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import DetalleIndependienteForm, IndependienteForm
from .models import Independiente, Comentario, Servicio
from .mail import Mail


def index(request):
    listaidependientes = Independiente.objects.all().order_by('fechaRegistro')
    context = {'listaidependientes': listaidependientes}
    return render(request, 'componentes/index.html', context)


def index_por_servicio(request, value):
    if request.method == 'GET':
        try:
            if value == -1:
                listaidependientes = Independiente.objects.all().order_by('fechaRegistro')
            else:
                id_servicio = value
                listaidependientes = Independiente.objects.filter(idServicio=id_servicio).order_by('fechaRegistro')
                context = {'listaidependientes': listaidependientes}
                return render(request, 'componentes/index.html', context)
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


def register(request):
    return render(request, 'componentes/register.html')


def login(request):
    return render(request, 'componentes/login.html')


def perfil(request):
    return render(request, 'componentes/perfil.html')


@csrf_exempt
def post_register(request):
    try:
        freelance = Independiente(
            nombre=request.POST['nombre'],
            apellidos=request.POST['apellidos'],
            aniosExperiencia=request.POST['aniosExperiencia'],
            idServicio=Servicio.objects.get(id=request.POST['idServicio']),
            telefono=request.POST['telefono'],
            correoElectronico=request.POST['correoElectronico'],
            contrasenia=request.POST['contrasenia'],
            foto=request.POST['foto'])
        freelance.save()
        mail = Mail(freelance.correoElectronico, 'Bienvenido a la comunidad Busco Ayuda!',
                    'Hola ' + freelance.nombre + ', <br><br>En Busco Ayuda puedes inscribir y buscar servicios prestados por independientes en oficios varios! <br><br>Gracias por hacer parte de nuestra comunidad.')
        mail.send()
        return HttpResponse(json.dumps(freelance.id), content_type="application/json", status=200)
    except Exception as e:
        print (e.args)
        return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


@csrf_exempt
def get_service(request):
    try:
        result = serializers.serialize('json', Servicio.objects.all())
        return HttpResponse(result, content_type="application/json", status=200)
    except Exception as e:
        return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


@csrf_exempt
def post_login(request):
    try:
        freelance = Independiente.objects.get(correoElectronico=request.POST['correoElectronico'])
        if (freelance.contrasenia == request.POST['contrasenia']):
            return HttpResponse(json.dumps(freelance.id), content_type="application/json", status=200)
        else:
            return HttpResponse(json.dumps(freelance.correoElectronico + " " + freelance.contrasenia),
                                content_type="application/json", status=401)
    except Exception as e:
        return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


def detalle_independiente(request, value):
    queryset = Independiente.objects.filter(id=value)
    if request.POST:
        form = DetalleIndependienteForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        independiente = Independiente.objects.get(id=value)
        form = DetalleIndependienteForm(instance=independiente)
    return render(request, 'componentes/independiente_form.html', {'form': form})


@csrf_exempt
def actualizar_independiente(request, value):
    queryset = Independiente.objects.filter(id=value)
    if request.POST:
        instance = Independiente.objects.get(id=value)
        form = IndependienteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        independiente = Independiente.objects.get(id=value)
        form = IndependienteForm(instance=independiente)
    return render(request, 'componentes/perfil.html', {'form': form})


@csrf_exempt
def crear_comentario(request):
    if request.method == 'POST':
        try:
            json_comentario = json.loads(request.body)
            id_independiente = json_comentario['idIndependiente']
            correo_electronico = json_comentario['correoElectronico']
            texto = json_comentario['texto']
            freelance = Independiente.objects.get(id=id_independiente)
            nuevo_comentario = Comentario(idIdependiente=freelance, correoElectronico=correo_electronico, texto=texto)
            nuevo_comentario.save()
            mail = Mail(freelance.correoElectronico, 'Nuevo comentario en la comunidad Busco Ayuda!',
                        'Hola ' + freelance.nombre + ', <br><br>Realizaron un nuevo comentario sobre tus servicios: <i>' + texto + ' </i><br><br>Gracias por hacer parte de nuestra comunidad.')
            mail.send()
            return HttpResponse(serializers.serialize('json', [nuevo_comentario]))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


@csrf_exempt
def ver_comentarios(request, value):
    if request.method == 'GET':
        try:
            comentarios = Comentario.objects.filter(idIdependiente=value)
            return HttpResponse(serializers.serialize('json', comentarios))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


@csrf_exempt
def ver_independientes_por_filtro(request, value):
    if request.method == 'GET':
        try:
            if value == -1:
                independientes = Independiente.objects.all().order_by('fechaRegistro')
            else:
                id_servicio = value
                independientes = Independiente.objects.filter(idServicio=id_servicio).order_by('fechaRegistro')
            return HttpResponse(serializers.serialize('json', independientes))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


@csrf_exempt
def ver_servicios(request):
    if request.method == 'GET':
        try:
            servicios = Servicio.objects.all()
            return HttpResponse(serializers.serialize('json', servicios))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


def api_independientes(request):
    if request.method == 'GET':
        try:
            independientes = Independiente.objects.all().order_by('fechaRegistro')
            return HttpResponse(serializers.serialize('json', independientes))

        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

    elif request.method == 'POST':
        try:
            independiente = Independiente(
                nombre=request.POST['nombre'],
                apellidos=request.POST['apellidos'],
                aniosExperiencia=request.POST['aniosExperiencia'],
                idServicio=Servicio.objects.get(id=request.POST['idServicio']),
                telefono=request.POST['telefono'],
                correoElectronico=request.POST['correoElectronico'],
                contrasenia=request.POST['contrasenia'],
                foto=request.POST['foto'])
            independiente.save()
            mail = Mail(independiente.correoElectronico, 'Bienvenido a la comunidad Busco Ayuda!',
                        'Hola ' + independiente.nombre + ', <br><br>En Busco Ayuda puedes inscribir y buscar servicios prestados por independientes en oficios varios! <br><br>Gracias por hacer parte de nuestra comunidad.')
            mail.send()
            return HttpResponse(json.dumps(independiente.id), content_type="application/json", status=200)
        except Exception as e:
            print (e.args)
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

def api_independientes_por_id(request, value):
    if request.method == 'GET':
        print value
        independiente = Independiente.objects.get(id=value)
        return HttpResponse(serializers.serialize('json', [independiente]))

    elif request.method == 'PUT':
        try:
            json_independiente = json.loads(request.body)
            independiente = Independiente(
                nombre=json_independiente['nombre'],
                apellidos=json_independiente['apellidos'],
                aniosExperiencia=json_independiente['aniosExperiencia'],
                idServicio=Servicio.objects.get(json_independiente['idServicio']),
                telefono=json_independiente['telefono'],
                correoElectronico=json_independiente['correoElectronico'],
                contrasenia=json_independiente['contrasenia'],
                foto=json_independiente['foto'])
            independiente.save()
            return HttpResponse(json.dumps(independiente.id), content_type="application/json", status=200)
        except Exception as e:
            print (e.args)
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)


def api_independientes_por_servicio(request, value):
    if request.method == 'GET':
        try:
            if value == -1:
                independientes = Independiente.objects.all().order_by('fechaRegistro')
            else:
                id_servicio = value
                independientes = Independiente.objects.filter(idServicio=id_servicio).order_by('fechaRegistro')
            return HttpResponse(serializers.serialize('json', independientes))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

def api_login(request):
    try:
        independiente = Independiente.objects.get(correoElectronico=request.POST['correoElectronico'])
        if (independiente.contrasenia == request.POST['contrasenia']):
            return HttpResponse(json.dumps(independiente.id), content_type="application/json", status=200)
        else:
            return HttpResponse(json.dumps(independiente.correoElectronico + " " + independiente.contrasenia),
                                content_type="application/json", status=401)
    except Exception as e:
        return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

def api_servicios(request):
    if request.method == 'GET':
        try:
            servicios = Servicio.objects.all()
            return HttpResponse(serializers.serialize('json', servicios))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

def api_comentarios(request):
    if request.method == 'POST':
        try:
            json_comentario = json.loads(request.body)
            id_independiente = json_comentario['idIndependiente']
            correo_electronico = json_comentario['correoElectronico']
            texto = json_comentario['texto']
            independiente = Independiente.objects.get(id=id_independiente)
            nuevo_comentario = Comentario(idIdependiente=independiente, correoElectronico=correo_electronico, texto=texto)
            nuevo_comentario.save()
            mail = Mail(independiente.correoElectronico, 'Nuevo comentario en la comunidad Busco Ayuda!',
                        'Hola ' + independiente.nombre + ', <br><br>Realizaron un nuevo comentario sobre tus servicios: <i>' + texto + ' </i><br><br>Gracias por hacer parte de nuestra comunidad.')
            mail.send()
            return HttpResponse(serializers.serialize('json', [nuevo_comentario]))

        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

def api_comentarios_por_independiente(request, value):
    if request.method == 'GET':
        try:
            comentarios = Comentario.objects.filter(idIdependiente=value)
            return HttpResponse(serializers.serialize('json', comentarios))
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)