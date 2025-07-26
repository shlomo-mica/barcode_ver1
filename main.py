# from __future__ import print_function
# import time
# import cloudmersive_barcode_api_client
# from cloudmersive_barcode_api_client.rest import ApiException
# from pprint import pprint
# YOUR_API_KEY='9fa74e71-bc0c-40df-9593-ef8d9c661d68'
# # Configure API key authorization: Apikey
# configuration = cloudmersive_barcode_api_client.Configuration()
# configuration.api_key['Apikey'] = YOUR_API_KEY
#
#
#
# # create an instance of the API class
# api_instance = cloudmersive_barcode_api_client.BarcodeLookupApi(cloudmersive_barcode_api_client.ApiClient(configuration))
# value = '0 71234 56789 ' # str | Barcode value
#
# try:
#     # Lookup EAN barcode value, return product data
#     api_response = api_instance.barcode_lookup_ean_lookup(value)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling BarcodeLookupApi->barcode_lookup_ean_lookup: %s\n" % e)

# CREATE  PNG FILE WITH THE CLOUDMERSIVE API (USING OUR API NUMBER)
from __future__ import print_function
import time
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException
from pprint import pprint
from barcode_image_show import barcode_Label_creation

Label_object = barcode_Label_creation
YOUR_APbI_KEY = '9fa74e71-bc0c-40df-9593-ef8d9c661d68'
# Configure API key authorization: Apikey
configuration = cloudmersive_barcode_api_client.Configuration()
configuration.api_key['Apikey'] = '9fa74e71-bc0c-40df-9593-ef8d9c661d68'
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
