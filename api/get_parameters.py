import requests
import json

      #API                                      # Parameter "timeZone" = Asia/Seoul
url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

r = requests.get(url)
print(r.text)


url = "https://timeapi.io/api/Time/current/zone"
parameters = {"timeZone": "Asia/Tokyo"}
r = requests.get(url, params=parameters)
print(r.text)

# Json to Dict 1
d = json.loads(r.text)
print(type(d))
# Json to Dict 2
d2 = r.json()
print(type(d2))


