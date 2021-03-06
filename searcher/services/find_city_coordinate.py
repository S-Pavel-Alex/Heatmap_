from warm.models import City, CoordinateCity
from yandex_geocoder import Client
from secret import api_key

client = Client(api_key=api_key)  # API yandex объект для конвертации


def find_city_coordinate():
    """
    Функция конвертации адреса в координаты
    """
    CoordinateCity.objects.all().delete()  # Очищается база при обновдении
    cities = City.objects.all()
    for city in cities:
        # Конвертер адреса в координаты от яндкса
        coordinates = client.coordinates(city.name)
        cord = CoordinateCity(
            latitude=float(coordinates[1]), longitude=float(coordinates[0]), city=city
        )
        cord.save()
