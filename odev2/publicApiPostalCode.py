### Ödev - 2 Public Api ###

import requests
import xmltodict
import pandas as pd

country = input("Ülke kodunu giriniz (ör: tr) :")
postal_code = input("Posta kodunu giriniz (ör: 34880) :")
print(country+ " / " +postal_code)

url =f"https://api.zippopotam.us/{country}/{postal_code}"
reponse = requests.get(url)

if reponse.status_code == 200:
    data = reponse.json()
    print(data)
else:
    print("api isteği başarısız oldu.")