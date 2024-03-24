#!/usr/bin/python3
"""
This script sends an HTTP GET request to the specified URL
and prints the response content.
If an HTTP error occurs, it prints the corresponding error code.
If a URL error occurs,
it prints the reason for the error.
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    # The URL to which the request will be sent
    url = sys.argv[1]

    # Create a Request object with the URL
    req = urllib.request.Request(url)

    try:
        # Send the request and read the response
        with urllib.request.urlopen(req) as response:
            content = response.read()
            # Print the response content after decoding it from utf-8
            print("{}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        # If an HTTPError occurs, print the error code
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        # If a URLError occurs, print the reason for the error
        print(e.reason)
