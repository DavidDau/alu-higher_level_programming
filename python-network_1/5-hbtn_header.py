#!/usr/bin/python3
"""
This script retrieves the value of the "X-Request-Id"
header from an HTTP GET request to a specified URL
using the requests library and prints the retrieved value.
"""

import requests
import sys

if __name__ == '__main__':
    # Get the URL from the command line argument
    url = sys.argv[1]

    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Retrieve the value of the "X-Request-Id" header
    x_request_id = response.headers.get("X-Request-Id")

    # Print the retrieved value
    print("{}".format(x_request_id))
