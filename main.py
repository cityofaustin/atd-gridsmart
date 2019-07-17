import pandas as pd
import requests

#reading local file for ips

df = pd.read_csv("grid_smarts.csv")
IP_Adds = df['Detector IP'].dropna().tolist()

#cleaning up ips

for x in range(len(IP_Adds)):
   IP_Adds[x] = IP_Adds[x].strip()

def Remove(duplicate=[]):
   IPs = []
   for uni in duplicate:
       if uni not in IPs:
           IPs.append(uni)
   return IPs

Unique_IPs = Remove(IP_Adds)

#the following section is for checking the status of the ips
goodvevil = dict()

for x in range(len(Unique_IPs)):
   ip = Unique_IPs[x]
   print("Checking status for camera: " + ip)
   try:
       #this sections makes an http request, might need to add checks for multiple cameras?
       status = requests.get(f'https://{ip}:8902/api/camera', timeout=10)
       print("Status: " + status.text)
       goodvevil[ip] = "ActiveCamera" in status.text


   except requests.exceptions.RequestException as e:
       #this catches errors for the http request and marks the ip as offline
       print("Exception for: " + ip + ", message: " + str(e))
       goodvevil[ip] = False

for key, value in goodvevil.items():
  print(key, value)


