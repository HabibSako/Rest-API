### Ödev 2 public api -> publicApiPostalCode'dur. Bu projede hatalar mevcuttur. ###
import requests
import pandas as pd

url = "https://ergast.com/api/f1/2008/5/results.json"
response = requests.get(url)

if response.status_code == 200:
    #apinin verdiği format csv olmadığı için günceleme (json veya xml olarak veriyor)
    data = response.json()["MRData"]["RaceTable"]["Races"][0]["Results"]
    df = pd.json_normalize(data)
    print(df.to_csv(index=False))
else:
    #hata kodu döndürme
    print(response.status_code)
    print("Api isteğiniz başarısız oldu.")

########################################## Deneme - Çalışmıyor #############################

# import requests
# import xmltodict
# import pandas as pd

# year = input("Yarış yılını giriniz (ör: 2020) :")
# round = input("Öğrenmek istediğiniz turu giriniz (ör: 4) :")
# print(year+ " / " +round)

##### yarış sonuçları #####
# url ="https://ergast.com/api/f1/{year}/{round}/results.json"

##### sıralamalar #####
#url ="https://ergast.com/api/f1/{year}/{round}/driverStandings.json"

# reponse = requests.get(url)
#
# if reponse.status_code == 200:
#     data = reponse.json()
#     df = pd.json_normalize(data)
#     print(df.to_csv(index=False))
# else:
#     print("api isteği başarısız oldu.")
#print(data)
##### xml olarak yazdırma #####

#xml_data = xmltodict.unparse(data)
#print(xml_data)




