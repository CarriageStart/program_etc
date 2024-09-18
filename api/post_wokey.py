
import json
import requests

def main():
    url = "https://timeapi.io/api/Conversion/ConvertTimeZone"

    header = {"Content-Type": "application/json"}

    json_data = json.dumps({
        "fromTimeZone": "Asia/Seoul",
        "dateTime": "2022-10-03 10:03:00",
        "toTimeZone": "UTC",
        "dstAmbiguity": ""
    })

    # Post Request
    result_dict = requests.post(url, headers=header, data=json_data).json()
    print(result_dict)

    # For Json String data, headers is not needed.
    result_dict2 = requests.post(url, data=json_data).json() 
    print(result_dict2)



if __name__=="__main__":
    print("Execute main function")
    main()
    print("Fisnish main function")

