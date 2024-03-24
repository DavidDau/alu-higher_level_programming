#!/usr/bin/python3
"""
This script sends an HTTP GET request to
the specified URL using the requests library.
It prints the response content if the request is successful,
or an error code if an error occurs.
"""

import requests
import sys

if __name__ == '__main__':
    # Get the URL from the command line argument
    url = sys.argv[1]

    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    if response.status_code >= 400:
        # If an error occurs (status code >= 400), print the error code
        print("Error code: {}".format(response.status_code))
    else:
        # If the request is successful, print the response content
        print("{}".format(response.text))
