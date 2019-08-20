# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import knackpy
import os
import pandas as pd
import requests

#
# First, we need to gather sensitive data.
#
knack_field_id = os.getenv("GS_KNACK_FIELD_ID")
knack_object_id = os.getenv("GS_KNACK_OBJECT_ID")
knack_app_id = os.getenv("GS_KNACK_APP_ID")
knack_api_id = os.getenv("GS_KNACK_API_KEY")

#
# Gather GRIDSMART devices
#
gs_type = {
   'match': 'or',
   'rules': [{
        'field': knack_field_id,
        'operator': 'is',
        'value': 'GRIDSMART'
    }]
}

#
# Execute through Knackpy
#

knack_response = knackpy.Knack(
   obj=knack_object_id,
   app_id=knack_app_id,
   api_key=knack_api_id,
   filters=gs_type
)

#
# Iterate through each camera
#

# # For debugging purposes:
# for detector in knack_response.data_raw:
#     print(detector)

# print("Total Detectors Count: " + str(len(knack_response.data_raw)))
# print("Data Raw object type: " + str(type(knack_response.data_raw)))

# Cleaning up IP addresses, using a lambda function and output a list
detectors_ip_list = list(
    map(lambda nth_element: str(nth_element['DETECTOR_IP']).strip(), knack_response.data)
)

# Let's remove duplicates my getting unique keys from the dict.fromkeys function
Unique_IPs = list(dict.fromkeys(detectors_ip_list))

#the following section is for checking the status of the ips
goodvevil = dict()

for x in range(len(Unique_IPs)):
   ip = Unique_IPs[x]
   print("Checking status for camera: " + ip)
   try:
       #this sections makes an http request, might need to add checks for multiple cameras?
       status = requests.get(f'https://{ip}:8902/api/camera', timeout=10)
       print("Status: " + status.text)
       # "ActiveCamera" in status.text evaluates if the string is contained
       # in the status.text variable. The result of the evaluation (true or false)
       # will be then assigned to goodvevil[ip]
       goodvevil[ip] = "ActiveCamera" in status.text


   except requests.exceptions.RequestException as e:
       #this catches errors for the http request and marks the ip as offline
       print("Exception for: " + ip + ", message: " + str(e))
       goodvevil[ip] = False

for key, value in goodvevil.items():
  print(key, value)
