from django.urls import path
from .views import getNearestPoint, getShipping, index, setPoint

urlpatterns = [
    path('', index),
    path('getNearestPoint', getNearestPoint),
    path('getShipping', getShipping),
    path('setPoint', setPoint)
]
