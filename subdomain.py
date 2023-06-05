import requests
limit = 20
url = "https://www.virustotal.com/api/v3/domains/issuu.com/subdomains?limit="+str(limit)

headers = {
    "accept": "application/json",
    "x-apikey": "725975dd6ef61743153ffb90537035e42fef8aba79c4308a18e6009be9165879"
}
print("kiba")
#print(response)
print(url)

response = requests.get(url, headers=headers)
response = response.text
print(response)
f = open("response-db","w")
f.write(response)

