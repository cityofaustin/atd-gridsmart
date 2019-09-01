#For now, we'll make a skeleton of what the code will hopefully look like once we can get access figured out.

#Imported arrow and requests because Knackpy's github documentation mentions needing it. 
import knackpy
import os
import requests
import arrow


#
# Gather GRIDSMART devices (borrowed from automate_gridsmart.py)
#
#gs_type = {
#   'match': 'or',
#   'rules': [{
#        'field': knack_field_id,
#        'operator': 'is',
#        'value': 'GRIDSMART'
#    }]
#}

#Execute through knackpy, borrowed from the automate_gridsmart.py script, since we will be retrieving data from
#the same object anyways.

#knack_response = knackpy.Knack(
#   obj=knack_object_id,
#   app_id=knack_app_id,
#   api_key=knack_api_id,
#   filters=gs_type
#)

# Cleaning up IP addresses, using a lambda function and output a list
# again, from automate_gridsmart.py
#detectors_ip_list = list(
#    map(lambda nth_element: str(nth_element['DETECTOR_IP']).strip(), knack_response.data)
#)

# Let's remove duplicates my getting unique keys from the dict.fromkeys function
#from automate_gridsmart.py
#Unique_IPs = list(dict.fromkeys(detectors_ip_list))

#Now we can try to ping our individual IPs and such... first let's make the simple version.
inputIp = input("Please input an IP: ")
try:
	req = requests.get("http://%s:8902/api" % inputIp)
	#req = requests.get("http://%s/" % inputIp)
	if req.status_code == 200:
		print("Success at IP: " + inputIp)
	else:
		print("Failed at IP: " + inputIp)
except Exception as e:
	print ("Failed at IP " + inputIp + ", reason was: " + str(e))
