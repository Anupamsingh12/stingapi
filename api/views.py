from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer,serializers
from rest_framework.decorators import api_view
import numpy as np
import pickle
import os
from .models import ml_model
from django.core import serializers
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def index(request):
    return render(request,'index.html')


st={ "age": "12","gender": "0",
"height": "168",
"weight": "72",
"ap_hi": "156",
"ap_low": "50",
"cholesterol": "1",
"gluc": "3",
"smoke": "0",
"alco": "1",
"active": "1" }
@csrf_exempt
def cardio_risk(request):
    if request.method == 'POST':
        filename='api/finalized_model2.sav'  
        loaded_model = pickle.load(open(filename, 'rb'))
        p=JSONParser().parse(request)
        p=p.data
        x=[]
        for a in p:
            x.append(int(p[a]))
        aa=np.array([x])
        aa.reshape(-1,1)
        xx=loaded_model.predict_proba(aa)
        return JsonResponse({"message": "cardio risk ", "data": xx})
    if request.method == 'GET':
        
        
        return JsonResponse({"message": "get request not allowed please send response as shown ","data":st})
   
    
   
    return JsonResponse({"message": "please send response as shown in documentation"})

@api_view(['GET', 'POST'])
def cardiorisk(request):
   
    if request.method == 'POST':
        filename='api/finalized_model2.sav'  
        loaded_model = pickle.load(open(filename, 'rb'))
        p=JSONParser().parse(request)
        
        x=[]
        for a in p:
            x.append(int(p[a]))
        aa=np.array([x])
        aa.reshape(-1,1)
        xx=loaded_model.predict_proba(aa)
        return Response({"message": "cardio risk", "data": xx})
       
    return Response({"message": "please send data in format ",'data':st})
