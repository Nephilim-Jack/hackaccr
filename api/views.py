from django.http import JsonResponse, HttpResponse
from .utils import calculateDistance, calculateShipping
from .models import Point

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


def setPoint(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')

        restaurant = request.GET.get('restautant')
        sleep = request.GET.get('sleep')
        secure = request.GET.get('secure')

        point = Point(
            name=name,
            latitude=lat,
            longitude=lng,
            hasRestaurant=restaurant,
            hasSleepPoint=sleep,
            isSecure=secure
        )

        point.save()
        return HttpResponse('succefuly added point to database')
