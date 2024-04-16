import requests

postcode_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(postcode_req)
# print(type(postcode_req.status_code))
# print(postcode_req.headers)
# print(type(postcode_req.content))
# print(postcode_req.json())

data_dict = postcode_req.json()["result"]
print(data_dict["region"])