# Heatmap
## This project creat web page in which is showed:
* Heatmaps for 3 cities which created on data: price and location apartment
* Histograms for 3 cities which created on data: averege price in district and averege meters in district
---
__Instraction__

Run server:
* in console write:  ___python manage.py runserver___
---
## Using:
1. In ___create_table_city.py___ you can see __INFO_LIST__ is dictionary with slugs and names cities
2. If going to domain/heatmap/slug from INFO_LIST then it will be page with heatmap for city
3. If going to domain/histogram/slug from INFO_list then it will be page with heatmap for city
4. Updata databasae in cosole write: python manage.py updata_database, but must have yandex [API key for HTTP](https://passport.yandex.ru/) 
5. API key using in __converter_coordinate.py__, __district_finder.py__, __find_city_coordinate__ 
