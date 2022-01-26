import matplotlib.pyplot as plt
from django.db.models import *

from warm.models import *


def create_histogram(city_name: City):
    """
    Функция построения 2 гистограм:
    1. гистограмма зависимости средней цены по муниципальному округу от
    муницыпального округа;
    2. гистограмма зависимости средней площади по муниципальному округу от
    муницыпального округа;
    """
    districts = District.objects.all().filter(address__city=city_name)

    # Создаем множество для отбора уникальных значений муницыпальных округов
    # Которые будут по оси х
    # Делается через set т.к. MySQL не поддерживает функцию disinkt()
    district_x_coordinate = set()
    # Создаем словари для координат по оси у - средняя цена и средняя площадь
    price_y_coordinate = {}
    meters_y_coordinate = {}
    # Создаем уникальные значения для муниципальных округов
    for district in districts:
        district_x_coordinate.add(district.district)
    # Формируем словари для привязки координат по оси х и у
    for coordinate in district_x_coordinate:
        # Ключ в словаре это уникальное имя  муниципального округа, значение
        # это отфильтрованная по муницапальному округу, и вычисленные среднее
        # значение цены и квадратных метров соответственно, округленное до 1
        # знака после запятой
        price_y_coordinate[coordinate] = round(
            District.objects.filter(district=coordinate).aggregate(
                res=Avg("address__price")
            )["res"],
            1,
        )
        meters_y_coordinate[coordinate] = round(
            District.objects.filter(district=coordinate).aggregate(
                res=Avg("address__meters")
            )["res"],
            1,
        )
    # Cоздаем полотно на котором будет располагать график зависимости цены
    # от мун. округа размера 25 на 15
    fig_price = plt.figure(figsize=(25, 15))
    # Создаем график на полотне
    ax_price = fig_price.subplots()
    # Cоздаем полотно на котором будет располагать график зависимости метров
    # от мун. округа размера 25 на 15
    fig_meters = plt.figure(figsize=(25, 15))
    # Создаем график на полотне
    ax_meters = fig_meters.subplots()
    # Передаем графику вида гистограмма, список координат по оси х и у
    ax_price.bar(price_y_coordinate.keys(), price_y_coordinate.values())
    ax_meters.bar(meters_y_coordinate.keys(), meters_y_coordinate.values())
    # Задаем название графика
    ax_price.set_title("Гистограмма цены")
    ax_meters.set_title("Гистограмма средней площади")
    # Задаем назавание оси х
    ax_price.set_xlabel("Муницыпальный округ")
    ax_meters.set_xlabel("Муницыпальный округ")
    # Задаем название оси у
    ax_price.set_ylabel("Средняя цена")
    ax_meters.set_ylabel("Средняя площадь")
    # Задаем угол наклона подписей координа на осях и их размер 45 и 7
    # соответственно
    ax_price.tick_params(labelrotation=45, labelsize=7)
    ax_meters.tick_params(labelrotation=45, labelsize=7)
    # Сохраняем нааши полотна по заданному пути и с заданным названием
    fig_price.savefig(f"warm/static/{city_name.slug}_price.png")
    fig_meters.savefig(f"warm/static/{city_name.slug}_meters.png")
    # Сохраняем полотна в бд
    Histogram(
        histogram_price_district=f"warm/static/" f"{city_name.slug}_price.png",
        histogram_meters_district=f"warm/static/" f"{city_name.slug}_meters.png",
        city=city_name,
    ).save()
