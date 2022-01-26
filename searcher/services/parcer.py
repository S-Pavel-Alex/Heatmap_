from warm.models import Address, City
import requests
from bs4 import BeautifulSoup
import time


def parcer(name: City, slug: str):
    """
    Парсер для забора информации о продаваемой недвижимлсти, парсинг
    осуществляется с сайта яндекс недвижимость.
    :param slug: slug взятый из базы данных
    :param name: обект города
    """

    all_pages = 2  # Количество страниц, которые нужно спарсить с сайта
    # недвижимости, такое маленькое число ограничено количесвом запросов
    # для конвертации
    for page in range(1, all_pages + 1):
        # Адрес сайти яндекс недвижимости
        url = f"https://realty.yandex.ru/{slug}/kupit/kvartira/?page={page}"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")
        card_apartments = soup.find_all(class_="OffersSerpItem__main")
        for card_apartment in card_apartments:
            info_address = card_apartment.find(class_="OffersSerpItem__generalInfo")
            meters = (
                info_address.find("a").find("h3", class_="OffersSerpItem__title").text
            )
            meters = float(meters.split("м²")[0].strip().replace(",", "."))
            address = info_address.find(class_="OffersSerpItem__address").text
            price = (
                card_apartment.find(class_="OffersSerpItem__dealInfo")
                .find("div", class_="OffersSerpItem__price-detail")
                .text
            )
            price = int(price.split("₽")[0].replace(" ", ""))
            address_object = Address(
                address=f"{name.name}, {address}", price=price, meters=meters, city=name
            )
            address_object.save()
        print(f"{page}")  # Отсчет отработанных странииц
        time.sleep(5)  # Антибан для сайта
