import requests

url = "https://api.azionapi.net/edge_applications"



payload={}
headers = {
  'Accept': 'application/json; version=3',
  'Authorization': 'Token %{}'.format()
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
