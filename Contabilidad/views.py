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
import json
import datetime
from bson.json_util import dumps, RELAXED_JSON_OPTIONS

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
def generarReporte(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.facturas
    facturas = db['facturas']
    fechaPrueba = datetime.datetime(2019,11,1)
    print(fechaPrueba)
    # delDia = facturas.find({"fecha" : request.POST.get("fecha", "")})
    # delDia = facturas.find({"fecha" : fechaPrueba})
    delDia = facturas.find({})
    result = []
    for data in delDia:
        result.append(data)
    client.close()
    print(str(result))
    return JsonResponse(json.loads(dumps(result, json_options = RELAXED_JSON_OPTIONS)), safe=False)