#!/usr/bin/python3
"""
This script sends a POST request to the specified URL
with an email as form data.
It then prints the response content decoded in utf-8.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    # The URL to which the request will be sent
    url = sys.argv[1]

    # The form data to be sent with the request, containing an email address
    values = {"email": sys.argv[2]}

    # Encode the form data to be sent in the request body
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Convert the encoded string to bytes

    # Create a Request object with the URL and the encoded data
    req = urllib.request.Request(url, data)

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        content = response.read()
        # Print the response content after decoding it from utf-8
        print("{}".format(content.decode("utf-8")))
