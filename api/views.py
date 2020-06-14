from django.shortcuts import render
from .utils import calculateDistance, calculateShipping

# Create your views here.


def getNearestPoint(request):
    if request.method == 'GET':
        locationsGeo = []
        actualGeo = [request.GET.get('lat'), request.GET.get('lng')]
        calculateDistance(actualGeo, locationsGeo)
