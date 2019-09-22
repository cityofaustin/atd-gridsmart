#Basically a variation on the old automate_gridsmart.py script.  Now it checks two ports with its requests! 
# - William Howland

#Imported arrow and requests because Knackpy's github documentation mentions needing it. 
import knackpy
import os
import requests
import arrow


#
# First, we need to gather sensitive data.
#
# (Borrowed from automate_gridsmart.py)
knack_field_id = os.getenv("GS_KNACK_FIELD_ID")
knack_object_id = os.getenv("GS_KNACK_OBJECT_ID")
knack_app_id = os.getenv("GS_KNACK_APP_ID")
knack_api_id = os.getenv("GS_KNACK_API_KEY")
#
# Gather GRIDSMART devices (borrowed from automate_gridsmart.py)
#
gs_type = {
   'match': 'or',
   'rules': [{
        'field': knack_field_id,
        'operator': 'is',
        'value': 'GRIDSMART'
    }]
}

#Execute through knackpy, borrowed from the automate_gridsmart.py script, since we will be retrieving data from
#the same object anyways.

knack_response = knackpy.Knack(
   obj=knack_object_id,
   app_id=knack_app_id,
   api_key=knack_api_id,
   filters=gs_type
)

# Cleaning up IP addresses, using a lambda function and output a list
# again, from automate_gridsmart.py
detectors_ip_list = list(
    map(lambda nth_element: str(nth_element['DETECTOR_IP']).strip(), knack_response.data)
)

# Let's remove duplicates my getting unique keys from the dict.fromkeys function
#from automate_gridsmart.py
Unique_IPs = list(dict.fromkeys(detectors_ip_list))

#Now we can try to make requests on GridSmarts.  
goodvevil = dict()

#Minor changes to this loop here: we are going to check the two ports that we know
#the Gridsmarts respond to now.
for x in range(len(Unique_IPs)):
    ip = Unique_IPs[x]
    print("Checking status for camera: " + ip)
    try:
        #this sections makes an http request, might need to add checks for multiple cameras?
        status = requests.get(f'http://{ip}:8902/api/camera', timeout=10)
        print("Status (port 8902): " + status.text)
        # "ActiveCamera" in status.text evaluates if the string is contained
        # in the status.text variable. The result of the evaluation (true or false)
        # will be then assigned to goodvevil[ip]
        goodvevil[ip] = "ActiveCamera" in status.text


    except requests.exceptions.RequestException as e:
        #this catches errors for the http request and marks the ip as offline
        print("Exception for: " + ip + " port 8902, message: " + str(e))
        goodvevil[ip] = False
    
    #second request, on another port!

    try:
        status = requests.get(f'http://{ip}:80/api/camera', timeout=10)
        print("Status (port 80): " + status.text)
        goodvevil[ip] = "ActiveCamera" in status.text
    

    except requests.exceptions.RequestException as e:
        print("Exception for: " + ip + " port 80, message: " + str(e))
        goodvevil[ip] = False
		
for key, value in goodvevil.items():
  print(key, value)
