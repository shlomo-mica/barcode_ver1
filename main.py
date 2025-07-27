
# CREATE  PNG FILE WITH THE CLOUDMERSIVE API (USING OUR API NUMBER)
from __future__ import print_function
import time
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException
from pprint import pprint
from barcode_image_show import barcode_Label_creation

Label_object = barcode_Label_creation
YOUR_APbI_KEY = 'aaaaaa'
# Configure API key authorization: Apikey
configuration = cloudmersive_barcode_api_client.Configuration()
configuration.api_key['Apikey'] = 'aaaaaa'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_barcode_api_client.GenerateBarcodeApi(
    cloudmersive_barcode_api_client.ApiClient(configuration))
value = '12345678901'  # str | UPC-A barcode value to generate from
Label_object()
try:
    # Generate a UPC-A code barcode as PNG file
    api_response = api_instance.generate_barcode_upca(value)
    pprint(api_response)

except ApiException as e:
    print("Exception when calling GenerateBarcodeApi->generate_barcode_upca: %s\n" % e)
