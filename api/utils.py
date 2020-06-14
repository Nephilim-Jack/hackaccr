from math import (sin, cos, radians, acos)


def calculateDistance(geo_in, geo_out):
    raio = 6371

    part_one = cos(radians(90-geo_in[0]))*cos(radians(90-geo_out[0]))
    part_two = sin(radians(90-geo_in[0]))*sin(radians(90-geo_out[0]))
    part_three = cos(radians(geo_in[1]-geo_out[1]))
    distance = raio*acos(part_one + part_two * part_three)

    return round(distance * 1000, 2)


def calculateShipping(distance, axes, cargoType):
    distance = int(distance)
    if cargoType == 'geral':
        if distance in list(range(101, 201)):
            basePrice = 1.35

    elif cargoType == 'granel':
        if distance in list(range(101, 201)):
            basePrice = 1.33

    elif cargoType == 'neogranel':
        if distance in list(range(101, 201)):
            basePrice = 1.21

    elif cargoType == 'frigo':
        if distance in list(range(101, 201)):
            basePrice = 0.95

    elif cargoType == 'perigosa':
        if distance in list(range(101, 201)):
            basePrice = 0.96

    value = distance * basePrice * int(axes)
    return value
