import json
import requests

ico=int(input("Zadejte ICO: "))
response2=requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data2=response2.json()
print(data2["obchodniJmeno"])
print(data2["sidlo"]["textovaAdresa"])

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
inp=str(input("Vyhledat: "))
data = {"obchodniJmeno": inp}
data_json=json.dumps(data)
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data_json)
response=res.json()
print(response["pocetCelkem"])
for i in response["ekonomickeSubjekty"]:
    print(i["obchodniJmeno"])


