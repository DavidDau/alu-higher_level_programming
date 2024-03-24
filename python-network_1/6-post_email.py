#!/usr/bin/python3
"""
This script sends an HTTP POST request to the specified URL
with an email address as form data.
It then prints the response content.
"""

import requests
import sys

if __name__ == '__main__':
    # Get the URL and email address from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send an HTTP POST request with the email address as form data
    response = requests.post(url, data={"email": email})

    # Print the response content
    print("{}".format(response.text))
