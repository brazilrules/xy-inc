from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_api.models import POI
from rest_api.serializers import POISerializer
import pdb

@csrf_exempt
def poi_list(request):
    if request.method == "GET":
        pois = POI.objects.all()
        serializer = POISerializer(pois, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = POISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

def search_near(request, coord_x, coord_y, distancia):
    if request.method == "GET":
        try:
            coord_x = int(coord_x)
            coord_y = int(coord_y)
            distancia = int(distancia)
        except TypeError:
            return HttpResponse("Todos os parametros devem ser números inteiros\nErro: TypeError", status=400)
        
        if coord_x < 0 or coord_y < 0 or distancia < 0:
            return HttpResponse("Todos os parametros devem ser positivos", status=400)
        
        pois = POI.objects.all()
        filtered_pois = []
        for poi in pois:
            distancia_x = abs(poi.coord_x - coord_x)
            distancia_y = abs(poi.coord_y - coord_y)
            if distancia_x <= distancia and distancia_y <= distancia:
                filtered_pois.append(poi)
        
        serializer = POISerializer(filtered_pois, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    return HttpResponse("Somente o método GET é aceito neste endpoint", status=400)