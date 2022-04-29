from warm.models import District, Coordinates
import requests
from secret import api_key


def district_finder():
    """
    Функция выполняющая GET запрос на сервис яндекса с координатами дома,
    возвращает, муниципальный округ, записывает в бд
    """
    District.objects.all().delete()  # Очищение базы данных для обновления
    coordinates = Coordinates.objects.all()
    for coordinate in coordinates:
        # Создаем GET запрос для получения муниципального округа из адреса
        # через яндекс сервис, ответ в формате json
        district = requests.get(
            f"https://geocode-maps.yandex.ru/1.x/?"
            f"format=json&"
            f"apikey={api_key}&"
            f"geocode={coordinate.longitude},"
            f"{coordinate.latitude}&"
            f"kind=district"
        )

        try:
            # Из ответа в формате json обращаемся к имене муниципального округа
            district = district.json()["response"]["GeoObjectCollection"]
            district = district["featureMember"][0]["GeoObject"]
            district = district["metaDataProperty"]["GeocoderMetaData"]["text"]
            district = district.split(",")[3]
            # Запись в бд
            mo_base = District(district=district, address=coordinate.address)
            mo_base.save()
            # Обработка исключения требуется из-за не идеальности яндекс
            # конвертера
        except IndexError:
            continue
