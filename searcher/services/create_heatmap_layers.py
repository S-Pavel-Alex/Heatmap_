from warm.models import *


def create_heatmap_layers(slug: str):
    """
    Функция сортирует координаты по цене, и полученый список
     делит на 5 списков, т.к. решено взять 5 цветовых оттенков по уровню цены
    :param slug: slug страницы города
    :return: 5 списков координат на каждый цветовой слой отражаущий уровень
     цены
    """
    # Получаем список координат отсортированных по цене
    coordinates = Coordinates.objects.filter(address__city__slug=slug).order_by(
        "address__price"
    )
    # Создаем список пар координат
    coordinate_for_layers = []
    # Добавляем пары в список
    for coordinate in coordinates:
        coordinate_for_layers.append([coordinate.latitude, coordinate.longitude])
    # Рассчитываем длинну  списков для каждого слоя
    part_coordinate_for_one_layer = len(coordinate_for_layers) // 5
    # Формируем списки кординат для каждого слоя
    very_small_price = coordinate_for_layers[0:part_coordinate_for_one_layer]
    small_price = coordinate_for_layers[
        part_coordinate_for_one_layer : 2 * part_coordinate_for_one_layer
    ]
    medium_price = coordinate_for_layers[
        2 * part_coordinate_for_one_layer : 3 * part_coordinate_for_one_layer
    ]
    medium_plus_price = coordinate_for_layers[
        3 * part_coordinate_for_one_layer : 4 * part_coordinate_for_one_layer
    ]
    high_price = coordinate_for_layers[
        4 * part_coordinate_for_one_layer : 5 * part_coordinate_for_one_layer
    ]
    return very_small_price, small_price, medium_price, medium_plus_price, high_price
