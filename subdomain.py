import requests
import re
import sys
import os
import subprocess
import json
def verify(domain,data):
	if "/" in data:
		pass
	else:
		print(data)
def monitor():
    headers = {
    	"Host": "dnsdumpster.com",
	"Cookie": "csrftoken=2sMhjDSIGgbmsE1cjPZdf3qJABZZP2baifoKvWbJEBfc8uqCh05Lo8V4ECZmXZhp; _ga=GA1.1.1684919107.1685350842;",
	"Content-Length": "124",
	"Upgrade-Insecure-Requests": "1",
	"Origin": "https://dnsdumpster.com",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Referer": "https://dnsdumpster.com/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9"
    }
    
    data = {
        "csrfmiddlewaretoken":"1AYxivP6rM3BAMjDHovBTSuyJYv94XTdhnA0uO87p77rgCI3FzB92XZTNZvwcUZs",
        "targetip":sys.argv[1],
        "user":"free",
    }
    r = requests.post(url="https://dnsdumpster.com/",headers=headers,data=data)
    f = open("/tmp/data","w")
    f.write(r.text)
    #os.system("grep -Po [a-z0-9.]+.issuu+.com /tmp/data")
    process = subprocess.Popen("grep -Po [a-z0-9.]+.issuu+.com /tmp/data", shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = process.communicate()
    out = str(out)
    out = out[2:]
    out1 = out.split("\\n")
    for o in out1:
    	verify(sys.argv[1],o)
def vt(url,limit):
	#limit = 20
	url = "https://www.virustotal.com/api/v3/domains/"+url+"/subdomains?limit="+str(limit)
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
	f.close()
def read_vt():
	f = open("response-db","r")
	data = f.read()
	f.close()
	data = json.loads(data)
	i = 0
	while(i<int(sys.argv[2])):
		try:
			print(data["data"][i]["id"])
		except:
			print("No more subdomains")
			sys.exit()
		i=i+1
monitor()
vt(sys.argv[1],sys.argv[2])
read_vt()
