#!/usr/bin/env python4

""" ISS Challenge: https://github.com/JasonTrespel/pythonexs/blob/main/API%20CHALLENGE-ISS.md """

# import requests
import requests
import datetime
import reverse_geocoder as rg

def main():
    """ Runtime code """

    api_link = "http://api.open-notify.org/iss-now.json"

    response = requests.get(f"{api_link}").json()
    
    # print translated json API response
    print(response)

    # variables for response data
    lon = response['iss_position']['longitude']
    lat = response['iss_position']['latitude']
    time = response['timestamp']
    converted_time = datetime.datetime.fromtimestamp(time)
    coordinates = (lat, lon)
    results = rg.search(coordinates)

    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {converted_time}\nLon: {lon}\nLat: {lat}\nCity/Country: {results[0]['name']}, {results[0]['cc']}")

if __name__ == "__main__":
    main()

