import knackpy
import os

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
for detector in knack_response.data_raw:
    print(detector[knack_field_id])