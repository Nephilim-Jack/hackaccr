from django.urls import path
from .views import getNearestPoint, getShipping, index

urlpatterns = [
    path('', index),
    path('getNearestPoint', getNearestPoint),
    path('getShipping', getShipping)
]
