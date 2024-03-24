#!/usr/bin/python3
"""
This script sends an HTTP request to the specified URL and
prints the value of the "X-Request-Id" header.
"""

import urllib.request
import sys

if __name__ == '__main__':
    # Get the URL from the command line argument
    url = sys.argv[1]

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Retrieve the headers from the response
        headers = response.info()

        # Print the value of the "X-Request-Id" header
        print(headers["X-Request-Id"])
