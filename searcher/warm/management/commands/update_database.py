from django.core.management.base import BaseCommand
from services.parcer import parcer
from services.created_table_city import create_table_city
from services.converter_coordinate import convert_coordinate
from services.district_finder import district_finder
from services.create_histogram import create_histogram
from services.find_city_coordinate import find_city_coordinate

from warm.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        City.objects.all().delete()  # Очищаем базу городов для обновления
        Address.objects.all().delete()  # Очищаем базу адресов для обновления
        create_table_city()  # Формируем таблицу городов
        find_city_coordinate()  # Находим и формируем таблицу с координатами
        # городов
        cities = City.objects.all()  # Запускаем парсер для все городов из
        # базы заносим в талицу адресов
        for city in cities:
            parcer(city, city.slug)
        convert_coordinate()  # Конвертируем адреса в координаты и заносим
        # в таблицу координат
        district_finder()  # По координатам находим муниципальные округа и
        # заносим в таблицу муниц. округов
        cities = City.objects.all()  # Создаем диаграммы
        Histogram.objects.all().delete()
        for city in cities:
            create_histogram(city)
