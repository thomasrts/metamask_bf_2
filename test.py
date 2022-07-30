import requests
import json

response = requests.get("https://api.ethplorer.io/getAddressInfo/0xae359bf7520EfD4aA3BEdeBda11340cDD7796253?apiKey=freekey").text
response = json.loads(response)
try:
    for key, value in response.items():
        if key == "tokens":
            for token in value:
                print("Token(s) found !")


except:
    pass