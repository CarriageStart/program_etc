
import json
import requests

def main():

    # Without Parameter
    url = "https://timeapi.io/api/TimeZone/AvailableTimeZones"
    result = requests.get(url)
    print(type(result)) # requests.models.Response Object
    print(result.text)  # Via "text" property, we can treat it as json string.

    p_dict = result.json()  # Convert Response Object(Json String) to python dict
    print(type(p_dict)) 
    print(p_dict)

    # With Parameter 1
    url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"
    result = requests.get(url)
    print(result.text)  

    # With Parameter 2
    url = "https://timeapi.io/api/Time/current/zone"
    parameter = {"timeZone": "Asia/Tokyo"}
    result = requests.get(url, params=parameter)
    print(result.text)  


if __name__=="__main__":
    print("Execute main function")
    main()
    print("Fisnish main function")

