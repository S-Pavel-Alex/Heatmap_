from warm.models import City

# Список slug и имен для городов
INFO_CITY = {
    "sankt-peterburg": "Санкт-Перербург",
    "moskva": "Москва",
    "ekaterinburg": "Екатеренбург",
}


def create_table_city():
    """
    Функция нополнения базы данных городами и слагами
    """
    City.objects.all().delete()
    for slug, name in INFO_CITY.items():
        City(name=name, slug=slug).save()
