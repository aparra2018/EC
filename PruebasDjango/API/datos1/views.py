from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import models
from datos1.models import datos1
from . import estadistica
import json
import base64

# Create your views here.
@api_view(['GET','POST','DELETE'])
def GetDatos(request,parametro):
    Datos=datos1.objects.filter(id=parametro)
    if(len(Datos)>0):
        Resp=Datos[0].datoT
    else:
        Resp=None
    if request.method=='GET':
        return Response({'Query':"Searching file with ID="+parametro,"file":Resp})

@api_view(['POST'])
def EstadisticaDesdeArchivo(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        if(len(archivo)>0):
            dato = json.loads(archivo)
            res = estadistica.Mostrar(dato,parametro1,parametro2)
            nom,val = estadistica.Suma(res)
            graf = [[nom,val]]
        return Response(graf)

@api_view(['POST'])
def ModaDesdeArchivo(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        estadigrafos=None
        if(len(archivo)>0):
            dato = json.loads(archivo)
            res = estadistica.Mostrar(dato,parametro1,parametro2)
            estadigrafos=estadistica.CalcularModa(res)
        return Response(estadigrafos)

@api_view(['POST'])
def MediaDesdeArchivo(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        estadigrafos=None
        if(len(archivo)>0):
            dato = json.loads(archivo)
            res = estadistica.Mostrar(dato,parametro1,parametro2)
            estadigrafos=estadistica.Comparador(res,estadistica.CalcularMedia,parametro1,parametro2)
        return Response(estadigrafos)

@api_view(['POST'])
def MedianaDesdeArchivo(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        estadigrafos=None
        if(len(archivo)>0):
            dato = json.loads(archivo)
            res = estadistica.Mostrar(dato,parametro1,parametro2)
            estadigrafos=estadistica.Comparador(res,estadistica.CalcularMediana,parametro1,parametro2)
        return Response(estadigrafos)

@api_view(['POST'])
def DesviacionEstandarDesdeArchivo(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        estadigrafos=None
        if(len(archivo)>0):
            dato = json.loads(archivo)
            res = estadistica.Mostrar(dato,parametro1,parametro2)
            estadigrafos=estadistica.Comparador(res,estadistica.CalcularDesviacionE,parametro1,parametro2)
        return Response(estadigrafos)

@api_view(['POST'])
def TablaFrecuenciaDesdeArchivo(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        estadigrafos=None
        if(len(archivo)>0):
            dato = json.loads(archivo)
            res = estadistica.Mostrar(dato,parametro1,parametro2)
            estadigrafos=estadistica.Comparador(res,estadistica.TablaFrecuencia,parametro1,parametro2)
        return Response(estadigrafos)

@api_view(['POST'])
def MostrarEnMapa(request):
    if request.method=='POST':
        parametro=request.data
        archivo=parametro[0]
        parametro1=str(parametro[1][1])
        parametro2=str(parametro[1][0])
        if(len(archivo)>0):
            dato = json.loads(archivo)
            if(parametro1=="lat" or parametro1=="lon"):
                res = estadistica.Mostrar(dato,"lat",parametro2)
                estadigrafos1=estadistica.Comparador(res,estadistica.DatosParaMapa,"lat",parametro2)
                res = estadistica.Mostrar(dato,"lon",parametro2)
                estadigrafos2=estadistica.Comparador(res,estadistica.DatosParaMapa,"lon",parametro2)
                return Response([estadigrafos1,estadigrafos2])
            elif(parametro2=="lat" or parametro2=="lon"):
                res = estadistica.Mostrar(dato,parametro1,"lat")
                estadigrafos1=estadistica.Comparador(res,estadistica.DatosParaMapa,parametro1,"lat")
                res = estadistica.Mostrar(dato,"lon",parametro2)
                estadigrafos2=estadistica.Comparador(res,estadistica.DatosParaMapa,"lon",parametro2)
                return Response([estadigrafos1,estadigrafos2])
            else:
                return Response(False)
        else:
                return Response(False)
        
            