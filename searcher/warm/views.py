from django.shortcuts import render, get_object_or_404
from services.create_heatmap_layers import create_heatmap_layers

from warm.models import *


def heatmap(request, slug: str):
    """
    Формирование ответа на зопрос по слагу
    :param request: запрос с слагом
    :param slug: слаг
    :return: html страницу с тепловой картой
    """
    city = get_object_or_404(City, slug=slug)
    # Получение координат города по слагу
    coordinates = CoordinateCity.objects.get(city__slug=slug)
    # Функция возвращает 5 списков координат, для разных слоев
    (
        very_small_price,
        small_price,
        medium_price,
        medium_plus_price,
        high_price,
    ) = create_heatmap_layers(slug=slug)
    title = city.name

    coordinate_city = [coordinates.latitude, coordinates.longitude]
    return render(
        request,
        "warm/heatmap.html",
        {
            "title": title,
            "coordinate_city": coordinate_city,
            "coordinates_very_small": very_small_price,
            "coordinates_small": small_price,
            "coordinates_medium": medium_price,
            "coordinates_medium_plus": medium_plus_price,
            "coordinates_high": high_price,
        },
    )


def histogram_page(request, slug: str):
    """
    Формирование ответа на зопрос по слагу
    :param request: запрос
    :param slug: слаг
    :return: html страницу с гистограммами
    """
    city = get_object_or_404(City, slug=slug)
    title = city.name
    return render(
        request,
        "warm/histogram.html",
        {
            "title": title,
            "histogram_price": city.slug + "_price.png",
            "histogram_meters": city.slug + "_meters.png",
        },
    )
