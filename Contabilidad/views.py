from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from rest_framework.parsers import JSONParser
from pymongo import MongoClient

@csrf_exempt
# Create your views here.
def guardarFactura(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.facturas
    facturas = db['facturas']
    data = JSONParser().parse(request)
    result = facturas.insert(data)
    respo ={
        "MongoObjectID": str(result),
        "Message": "nuevo objeto en la base de datos"
    }
    client.close()
    return JsonResponse(respo, safe=False)

@csrf_exempt
def buscarFactura(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.facturas
    facturas = db['facturas']
    results = []
    for factura in facturas:
        results.append(str(factura))
    client.close()
    return JsonResponse(results, safe=False)