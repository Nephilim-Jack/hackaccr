from django.http import JsonResponse, HttpResponse
from .utils import calculateDistance, calculateShipping

# Create your views here.


def index(request):
    return HttpResponse('main page of api use /getNearestPoint or /getShipping')


def getNearestPoint(request):
    if request.method == 'GET':
        locationsGeo = [-18.469, -44.589]
        actualGeo = [request.GET.get('lat'), request.GET.get('lng')]

        result = calculateDistance(actualGeo, locationsGeo)
        context = {'Posto Ficticio': result}

        return JsonResponse(context)


def getShipping(request):
    if request.method == 'GET':
        distance = int(request.GET.get('distance'))
        axes = int(request.GET.get('axes'))
        cargoType = str(request.GET.get('cargoType'))

        result = calculateShipping(distance, axes, cargoType)
        context = {'price': result}

        return JsonResponse(context)
