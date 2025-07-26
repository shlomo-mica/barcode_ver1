from __future__ import print_function
import time
from multiprocessing.pool import ApplyResult
from pprint import pprint
from datetime import date, datetime
from urllib3.response import BaseHTTPResponse
from urllib3._collections import HTTPHeaderDict
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException, RESTResponse
from urllib3 import BaseHTTPResponse
import requests

# Simulated response for demo purposes
api_response = {'key': 'value'}  # Replace this with your actual respons

# Simulated response for demo purposes

# Configure API key authorization: Apikey
configuration = cloudmersive_barcode_api_client.Configuration()
configuration.api_key['Apikey'] = '9fa74e71-bc0c-40df-9593-ef8d9c661d68'

# create an instance of the API class
api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
image_file = r'C:\Users\shlom\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\clcoding_barcode.png'  # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
image_2 = r'captured_images/barcode_pic1.png'
try:
    # Scan and recognize an image of a barcode
    api_response = api_instance.barcode_scan_image(image_2)
    pprint(api_response)
    result = api_response
    a = api_response
    print(a.raw_text)
    if a.successful:
        print(f"Barcode value: {a.raw_text}")

    print("Raw text:", result)
    if isinstance(result, dict):
        # Access key-value pairs
        data = result.get("barcode_data", None)

    elif isinstance(result, tuple):
        content, status_code, headers = result
        print("Content:", content)
        print("Status code:", status_code)
        print("Headers:", headers)

    elif isinstance(result, RESTResponse) or isinstance(result, BaseHTTPResponse):
        body = result.data  # Or check `.text`, `.json()`, depending on library

    elif isinstance(result, str):
        print("Raw text:", result[3])
        a = result[3]
        print('sfsf', a)
    elif isinstance(result, bytes):
        text = result.decode("utf-8")
        print("Decoded text:", text)

    # {'barcode_type': 'EAN_13', 'raw_text': '7290018282861', 'successful': True}


except ApiException as e:
    print("Exception when calling BarcodeScanApi->barcode_scan_image: %s\n" % e)
