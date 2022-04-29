from warm.models import Address, Coordinates
from yandex_geocoder import Client, exceptions
from secret import api_key

client = Client(api_key=api_key)  # API yandex объект для конвертации


def convert_coordinate():
    """
    Функция конвертации адреса в координаты и записывающая их в базу даных
    """
    Coordinates.objects.all().delete()  # Очищается база при обновдении
    addresses = Address.objects.all()
    for address in addresses:
        try:
            # Конвертер адреса в координаты от яндкса
            coordinates = client.coordinates(address.address)
            cord = Coordinates(
                latitude=float(coordinates[1]),
                longitude=float(coordinates[0]),
                address=address,
            )
            cord.save()
        # Адреса полученные с сайта могут быть не корректны, для этого
        # исключение пропускающее эти данные
        except exceptions.NothingFound:
            continue
